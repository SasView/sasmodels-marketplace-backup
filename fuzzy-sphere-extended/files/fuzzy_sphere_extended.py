r"""
Definition
----------
This model expands the fuzzy sphere model to include the high q contributions
associated with density fluctuations from self-avoiding random walk polymers.
The scattering intensity $I(q)$ is given as

..math::
    
    I(q) = \text{scale} \times V (\Delta \rho)^2 (P_{fs}(q) + P_{b}(q))


Where $P_{fs} = A(q)^2$ is the fuzzy sphere form factor.

..math::
    
    A(q) = \frac{3\left[\sin(qR) - qR \cos(qR)\right]}{(qR)^3}
           \exp\left(\frac{-(\sigma_\text{fuzzy}q)^2}{2}\right)


The $P_{b}(q)$ term accounts for the density fluctuations of polymer chains
within a 'blob' of radius, $\xi$ (i.e., the correlation length of the density
fluctuations), and is given by

..math::
    
    P_b(q) = \frac{a_b}{\mu q_b} \frac{\sin(\mu \arctan(q_b))}{(1+q_b^2)^{\mu/2}}
    \mu = \nu^{-1}-1
    q_b = \frac{q\xi}{\left[\text{erf}\left(\frac{qR_g}{\sqrt{6}}\right)\right]^3}


Where $\nu$ is the Flory-Huggins parameter, $R_g$ is the radius of gyration of
the polymer chain, and $a_b$ is the relative amplitude of $P_b(q)$ to $P_{fs}(q)$.

References
----------
#. S Rathgeber, M Monkenbusch, M Kreitschmann, V Urban, A Brulet,
    *J Chem Phys*, 117 (2002) 4047-4062
#. M Stieger, J. S Pedersen, P Lindner, W Richtering,
   *Langmuir*, 20 (2004) 7283-7292


Authorship and Verification
---------------------------

* **Author: Kush J Patel** --- **Date:** 2024YYY-01m-17d
* **Last Modified by:** --- **Date:** 2024YYY-01m-17d
* **Last Reviewed by:** --- **Date:** 2024YYY-01m-17d
"""

from sasmodels.special import *
from numpy import inf, arctan
from scipy.special import erf

name = "fuzzy_sphere_extended"
title = "User model for fuzzy_sphere_extended"
description = """"""

parameters = [ 
#   ["name", "units", default, [lower, upper], "type", "description"],
    ['sld', '1e-6/Ang^2', 3.0, [-inf, inf], 'sld', ''],    
    ['sld_solv', '1e-6/Ang^2', 1.0, [-inf, inf], 'sld', ''],
    ['R_sphere', 'Ang', 50.0, [0, inf], 'volume', ''],
    ['sig_fuzzy', 'Ang', 10.0, [0, inf], 'volume', ''],
    ['rel_amp', '', 0.01, [0, inf], '', ''],
    ['Rg', 'Ang', 30.0, [0, inf], 'volume', ''],
    ['FloryHuggins', '', 0.6, [-inf, inf], '', ''],
    ['corr_len', 'Ang', 15.0, [0, inf], 'volume', ''],
    ]
def Iq(x, sld, sld_solv, R, sig_fuzzy, rel_amp, Rg, FloryHuggins, corr_len):
    """Absolute scattering"""
    q = x
    mu = (FloryHuggins**-1)-1
    qb = q*corr_len/(erf(q*Rg/sqrt(6)))**3

    Pb = rel_amp/(mu*qb) * sin(mu*arctan(qb)) / (1+qb**2)**(mu/2)
    
    A = (3*(sin(q*R) - q*R*cos(q*R))/(q*R)**3)*exp(-((sig_fuzzy*q)**2)/2)
    
    sld_sqdiff = (sld - sld_solv)**2
    V = 4/3*pi*R**3
    
    y = sld_sqdiff*V*(Pb + A**2)*1e-4
    
    return y
## uncomment the following if Iq works for vector x
#Iq.vectorized = True

#def Iqxy(x, y, sld_solv, sld, rel_amp, R, sig_fuzzy, Rg, FH, corr_len):
#    """Absolute scattering of oriented particles."""
#    ...
#    return oriented_form(x, y, args)
## uncomment the following if Iqxy works for vector x, y
#Iqxy.vectorized = True
