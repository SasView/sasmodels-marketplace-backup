# fuzzy_sphere_extended

Definition ---------- This model expands the fuzzy sphere model to include the high q contributions associated with density fluctuations from self-avoiding random walk polymers. The scattering intensity $I(q)$ is given as $I(q) = \text{scale} \times V (\Delta \rho)^2 (P_{fs}(q) + P_{b}(q))$ Where $P_{fs} = A(q)^2$ is the fuzzy sphere form factor. $A(q) = \frac{3\left[\sin(qR) - qR \cos(qR)\right]}{(qR)^3} \exp\left(\frac{-(\sigma_\text{fuzzy}q)^2}{2}\right)$ The $P_{b}(q)$ term accounts for the density fluctuations of polymer chains within a 'blob' of radius, $\xi$ (i.e., the correlation length of the density fluctuations), and is given by $P_b(q) = \frac{a_b}{\mu q_b} \frac{\sin(\mu \arctan(q_b))}{(1+q_b^2)^{\mu/2}}$ $\mu = \nu^{-1}-1$ $q_b = \frac{q\xi}{\left[\text{erf}\left(\frac{qR_g}{\sqrt{6}}\right)\right]^3}$ Where $\nu$ is the Flory-Huggins parameter, $R_g$ is the radius of gyration of the polymer chain, and $a_b$ is the relative amplitude of $P_b(q)$ to $P_{fs}(q)$. References ---------- 1. S Rathgeber, M Monkenbusch, M Kreitschmann, V Urban, A Brulet, J Chem Phys, 117 (2002) 4047-4062 2. M Stieger, J. S Pedersen, P Lindner, W Richtering, Langmuir, 20 (2004) 7283-7292 Authorship and Verification --------------------------- * **Author: Kush J Patel** --- **Date:** 2024-01-17

Definition ---------- This model expands the fuzzy sphere model to include the high q contributions associated with density fluctuations from self-avoiding random walk polymers. The scattering intensity $I(q)$ is given as $I(q) = \text{scale} \times V (\Delta \rho)^2 (P_{fs}(q) + P_{b}(q))$

Where $P_{fs} = A(q)^2$ is the fuzzy sphere form factor.

$A(q) = \frac{3\left[\sin(qR) - qR \cos(qR)\right]}{(qR)^3} \exp\left(\frac{-(\sigma_\text{fuzzy}q)^2}{2}\right)$

The $P_{b}(q)$ term accounts for the density fluctuations of polymer chains within a 'blob' of radius, $\xi$ (i.e., the correlation length of the density fluctuations), and is given by

$P_b(q) = \frac{a_b}{\mu q_b} \frac{\sin(\mu \arctan(q_b))}{(1+q_b^2)^{\mu/2}}$ $\mu = \nu^{-1}-1$ $q_b = \frac{q\xi}{\left[\text{erf}\left(\frac{qR_g}{\sqrt{6}}\right)\right]^3}$

Where $\nu$ is the Flory-Huggins parameter, $R_g$ is the radius of gyration of the polymer chain, and $a_b$ is the relative amplitude of $P_b(q)$ to $P_{fs}(q)$.

References ---------- 1. S Rathgeber, M Monkenbusch, M Kreitschmann, V Urban, A Brulet, J Chem Phys, 117 (2002) 4047-4062 2. M Stieger, J. S Pedersen, P Lindner, W Richtering, Langmuir, 20 (2004) 7283-7292

Authorship and Verification ---------------------------

* **Author: Kush J Patel** --- **Date:** 2024-01-17

Source: https://marketplace.sasview.org/models/156/
