#!/usr/bin/env python3
"""
Scrape all models (code + page docs) from https://marketplace.sasview.org
and save outputs to subfolders named after each model.

Usage:
    python scrape_sasview_marketplace.py --out ./sasview_marketplace_dump --delay 1.0

What it does:
- Crawls the All Models index (with pagination) to collect model URLs.
- For each model:
  - Saves the full model page HTML to <out>/<model-slug>/model.html
  - Extracts a simple Markdown README from the description area to <out>/<model-slug>/README.md
  - Finds all file links in the "Files" section, opens each "View File" page,
    follows its "Download" link (raw file), and saves it to <out>/<model-slug>/files/<filename>
- Polite scraping: identifies with a User-Agent, retries, and sleeps between requests.

Tested against live structure as of 2025-09-30.
"""

import argparse
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://marketplace.sasview.org"
ALL_MODELS_URL = f"{BASE_URL}/models/"

# --- Utilities ----------------------------------------------------------------

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text or "model"

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def clean_filename(name: str) -> str:
    # preserve extensions; sanitize the stem
    name = name.strip().replace("\n", " ").replace("\r", " ")
    name = re.sub(r"[\\/:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", " ", name)
    return name

def make_session():
    s = requests.Session()
    s.headers.update({
        "User-Agent": "SciLifeLab-ModelHarvester/1.0 (+https://scilifelab.se) Python requests",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    })
    # Simple adapter retries
    try:
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        retry = Retry(
            total=5,
            read=5,
            connect=5,
            backoff_factor=0.5,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=frozenset(["GET", "HEAD"]),
        )
        s.mount("http://", HTTPAdapter(max_retries=retry))
        s.mount("https://", HTTPAdapter(max_retries=retry))
    except Exception:
        pass
    return s

def get_soup(session: requests.Session, url: str) -> BeautifulSoup:
    r = session.get(url, timeout=30)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")

def text_content(el) -> str:
    # Simple text extraction that keeps headings and paragraphs separate-ish
    parts = []
    for node in el.descendants:
        if node.name in ("h1", "h2", "h3", "h4"):
            parts.append(f"\n\n# {node.get_text(strip=True)}\n")
        elif node.name in ("p", "li"):
            txt = node.get_text(" ", strip=True)
            if txt:
                parts.append(txt)
    md = "\n\n".join(parts)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()

# --- Discovery ----------------------------------------------------------------

def discover_all_model_links(session: requests.Session, delay: float) -> list[str]:
    """
    Walk the All Models index, following pagination, return list of model page URLs.
    """
    model_urls = set()
    page = 1
    while True:
        url = ALL_MODELS_URL if page == 1 else f"{ALL_MODELS_URL}?page={page}"
        soup = get_soup(session, url)
        # On index/category pages, model links appear as anchors before the table columns
        # We’ll heuristically accept links that look like /models/<slug-or-id>/
        for a in soup.select("a[href]"):
            href = a.get("href")
            if not href:
                continue
            full = urljoin(BASE_URL, href)
            # Match /models/slug/ or /models/<id>/
            if re.search(r"/models/[^/]+/?$", urlparse(full).path) and not full.rstrip("/").endswith("/models"):
                model_urls.add(full.rstrip("/") + "/")
        # Try to detect "Page N of M" or presence of a "next" page
        page_text = soup.get_text(" ", strip=True)
        # The category page shows "Page 1 of 2" etc; stop when next page yields no new links
        prev_count = len(model_urls)
        # Heuristic: if the page has a "Page X of Y" and X >= Y, break; else try next page.
        m = re.search(r"Page\s+(\d+)\s+of\s+(\d+)", page_text, flags=re.I)
        if m:
            cur, total = int(m.group(1)), int(m.group(2))
            if cur >= total:
                break
        else:
            # If no pager text, stop when requesting a higher page returns no new links.
            # We will probe one extra page; if no new links, break.
            pass
        page += 1
        time.sleep(delay)
        # Safety: stop if too many pages
        if page > 100:
            break
        # If the next page has no new links, break.
        if page > 2:
            # lightweight probe
            probe_url = f"{ALL_MODELS_URL}?page={page}"
            try:
                soup_probe = get_soup(session, probe_url)
                new_links = 0
                for a in soup_probe.select("a[href]"):
                    href = a.get("href")
                    if not href:
                        continue
                    full = urljoin(BASE_URL, href)
                    if re.search(r"/models/[^/]+/?$", urlparse(full).path) and not full.rstrip("/").endswith("/models"):
                        if (full.rstrip("/") + "/") not in model_urls:
                            new_links += 1
                if new_links == 0:
                    break
            except requests.RequestException:
                break
            # consume this page properly
            for a in soup_probe.select("a[href]"):
                href = a.get("href")
                if not href:
                    continue
                full = urljoin(BASE_URL, href)
                if re.search(r"/models/[^/]+/?$", urlparse(full).path) and not full.rstrip("/").endswith("/models"):
                    model_urls.add(full.rstrip("/") + "/")
            page += 1
            time.sleep(delay)
            if page > 100:
                break

    return sorted(model_urls)

# --- Per-model scraping --------------------------------------------------------

def find_files_on_model_page(soup: BeautifulSoup) -> list[str]:
    """
    Return URLs of the 'Files' anchors on a model page. These are "View File" pages
    which usually contain a 'Download' link to the raw file.
    """
    file_urls = []
    # The "Files" list often appears as anchors near text "Files"
    # We’ll find anchors whose href path starts with /uploads/
    for a in soup.select("a[href]"):
        href = a.get("href")
        if not href:
            continue
        full = urljoin(BASE_URL, href)
        path = urlparse(full).path
        if path.startswith("/uploads/"):
            file_urls.append(full)
    return list(dict.fromkeys(file_urls))  # dedupe, preserve order

def find_download_link_on_viewfile_page(soup: BeautifulSoup) -> str | None:
    """
    Inside a /uploads/<id> "View File" page, there is usually a 'Download' link
    pointing at /uploads/uploaded_models/<filename>.
    """
    for a in soup.select("a[href]"):
        if a.get_text(strip=True).lower() == "download":
            href = a.get("href")
            if href:
                return urljoin(BASE_URL, href)
    # Fallback: look for links under /uploads/uploaded_models/
    for a in soup.select("a[href]"):
        href = a.get("href") or ""
        if "/uploads/uploaded_models/" in href:
            return urljoin(BASE_URL, href)
    return None

def guess_filename_from_url(u: str) -> str:
    path = urlparse(u).path
    name = os.path.basename(path)
    return clean_filename(name) or "file.bin"

def save_binary(session: requests.Session, url: str, dest: Path):
    r = session.get(url, timeout=60, stream=True)
    r.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

def scrape_model(session: requests.Session, model_url: str, out_root: Path, delay: float):
    soup = get_soup(session, model_url)
    # Title
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else urlparse(model_url).path.rstrip("/").split("/")[-1]
    slug = slugify(title)
    model_dir = out_root / slug
    files_dir = model_dir / "files"
    ensure_dir(files_dir)

    # Save full page HTML
    (model_dir / "model.url.txt").write_text(model_url, encoding="utf-8")
    (model_dir / "model.html").write_text(str(soup), encoding="utf-8")

    # Simple README from Description block if present
    # Heuristic: description often sits under an h2 with "Description"
    desc_block = None
    for hdr in soup.find_all(["h2", "h3"]):
        if "description" in hdr.get_text(strip=True).lower():
            # take siblings until next header
            parts = []
            for sib in hdr.next_siblings:
                if getattr(sib, "name", None) in ("h1", "h2", "h3"):
                    break
                if getattr(sib, "name", None) in ("p", "ul", "ol", "div", "pre"):
                    parts.append(sib)
            if parts:
                wrapper = BeautifulSoup("<div></div>", "html.parser")
                for p in parts:
                    wrapper.div.append(p if isinstance(p, (str,)) else p.extract())
                desc_block = wrapper.div
            break
    if not desc_block:
        # Fallback to the main content area (page body minus nav)
        main = soup
        readme_md = f"# {title}\n\nSource: {model_url}\n"
    else:
        readme_md = f"# {title}\n\n" + text_content(desc_block) + f"\n\nSource: {model_url}\n"
    (model_dir / "README.md").write_text(readme_md, encoding="utf-8")

    # Collect file "View File" pages
    viewfile_urls = find_files_on_model_page(soup)

    downloaded = 0
    for vf_url in viewfile_urls:
        try:
            vf_soup = get_soup(session, vf_url)
            # Save the View File HTML too (useful extra docs)
            vf_id = urlparse(vf_url).path.rstrip("/").split("/")[-1]
            (model_dir / f"viewfile_{vf_id}.html").write_text(str(vf_soup), encoding="utf-8")
            # Find the raw download link
            raw_url = find_download_link_on_viewfile_page(vf_soup)
            if raw_url:
                fname = guess_filename_from_url(raw_url)
                dest = files_dir / fname
                save_binary(session, raw_url, dest)
                downloaded += 1
            time.sleep(delay)
        except requests.RequestException as e:
            print(f"[WARN] Failed to fetch {vf_url}: {e}", file=sys.stderr)

    print(f"[OK] {title}  -> {downloaded} file(s)")
    time.sleep(delay)

# --- Main ---------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Scrape SasView Model Marketplace models and docs.")
    parser.add_argument("--out", required=True, help="Output directory root")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between HTTP requests (seconds)")
    #parser.add_argument("--base", default=BASE_URL, help="Base URL (default: https://marketplace.sasview.org)")
    args = parser.parse_args()

    out_root = Path(args.out)
    ensure_dir(out_root)

    #global BASE_URL, ALL_MODELS_URL
    #BASE_URL = args.base.rstrip("/")
    BASE_URL = "https://marketplace.sasview.org"
    ALL_MODELS_URL = f"{BASE_URL}/models/"

    session = make_session()

    try:
        print("[*] Discovering model pages...")
        model_urls = discover_all_model_links(session, delay=args.delay)
        if not model_urls:
            print("[!] No model URLs discovered. Is the site reachable?", file=sys.stderr)
            sys.exit(2)
        print(f"[*] Discovered {len(model_urls)} model page(s).")

        for i, u in enumerate(model_urls, 1):
            print(f"[*] ({i}/{len(model_urls)}) {u}")
            try:
                scrape_model(session, u, out_root, delay=args.delay)
            except requests.RequestException as e:
                print(f"[WARN] Failed to scrape model at {u}: {e}", file=sys.stderr)

        print("[✓] Done.")
        print(f"[i] Output saved under: {out_root.resolve()}")
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.", file=sys.stderr)
        sys.exit(130)

if __name__ == "__main__":
    main()

