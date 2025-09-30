# sasmodels-marketplace-backup

python scrape_sasview_marketplace.py --out ./sasview_marketplace_dump --delay 1.0

It crawls the “All Models” listing (across all pages), opens each model detail page, grabs any “Files” → “View File” pages, follows their “Download” links (e.g. /uploads/uploaded_models/*.py, .c, etc.), and saves everything under output/<model-slug>/. It also saves the model page HTML (for documentation) and a lightweight Markdown README extracted from the description block.
