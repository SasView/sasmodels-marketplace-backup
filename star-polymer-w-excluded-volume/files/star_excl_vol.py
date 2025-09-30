r"""
Definition
----------

This model implements the form factor for a star polymer with excluded volume, i.e., one in which the arms of the
polymer need not be ideal chains. Under this model, the scattering from a single arm of the polymer is described by:

.. math::

    P_{sb}(q,N) = frac{1}{
u U^{1/2
u}}gamma left( frac{1}{2
u}, Uight) - frac{1}{
u U^{1/
u}}gamma left(frac{1}{
u}, U ight)

where :math: `U = q^{2} b^{2} N^{2
u} / 6`, :math: `b` is the Kuhn length of the polymer, :math: `N` is the degree of polymerization of a single
arm of the polymer, and :math: `
u` is the excluded volume parameter / Flory exponent of the arm.

The scattering intensity is then given by:

.. math::
    I(q) = frac{1}{f^{2}} left[ fP_{sb}(q,N) + f(f-1)P_{ib}(q,N) ight]

where :math: `P_{ib}(q,N) = 2P_{sb}(q, 2N) - P_{sb}(q, N)`, and :math: `f` is the number of arms on the polymer. The intensity is scaled by the parameter
*scale* as well as the difference in scattering length density of the polymer and matrix.



References
----------

B. Hammouda, "Form Factors for Branched Polymers with Excluded Volume", J. of Research of NIST, 121, 139-164 (2016).
X. Lang, W. R. Lenart, J. E. P. Sun, B. Hammouda, and M. J. A. Hore, "Interaction and Conformation of Aqueous Poly(N-isopropylacrylamide) (PNIPAM) Star Polymers below the LCST", Macromolecules, 50, 2145-2154 (2017).

Authorship and Verification
----------------------------

* **Author:** Michael J. A. Hore **Date:** 16 Aug 2018
"""

import numpy as np
from numpy import inf, errstate, power,exp, sqrt
from scipy.special import gammainc, gamma

name = "star_excl_vol"
title = "Star polymer with excluded volume"
description = """
      List of default parameters:
      scale = Scaling factor
      nu = Excluded volume parameter
	  f = Number of arms
      b = Kuhn length
      n = Degree of polymerization
      sldp = Scattering length density of polymer
      slds = Scattering length density of solvent/matrix
      background = Incoherent background"""
category = "shape-independent"

# pylint: disable=bad-whitespace, line-too-long
#             ["name", "units", default,       [lower, upper], "type", "description"],
parameters = [
              ["nu",       "",                 0.5,       [0, 1],         "",     "Excluded volume parameter"],
              ["f",        "",                  3,        [1, inf],       "",     "Number of arms"],
              ["b",        "Ang",              7.0,       [1, inf],       "",     "Kuhn length"],
              ["n",        "",                30.0,       [1, inf],       "",     "Degree of polymerization"],
              ["sldp",     "1e-6/Ang^2",       1.4,       [-inf,inf],     "sld",  "Polymer SLD"],
              ["slds",     "1e-6/Ang^2",       6.7,       [-inf,inf],     "sld",  "Solvent SLD"],
             ]
# pylint: enable=bad-whitespace, line-too-long

def Iq(q,
       nu,
	   f,
       b,
       n,
       sldp,
       slds):
    """
    :param q:              Input q-value
    :param nu:             Excluded volume parameter
	:param f:              Number of arms
    :param b:              Kuhn length
    :param n:              Degree of polymerization
    :param sldp:           Polymer scattering length density
    :param slds:           Solvent scattering length density
    :return:               Calculated intensity
    """

    # Excl. Vol. Parameters
    onu  = 1.0/nu
    o2nu = 1.0/2.0/nu
 
    # Polymer chain form factor (single branch):
    U = q**2 * b**2 * power(n, 2.0*nu) / 6.0
    Psb = onu * power(U, -o2nu) * gamma(o2nu) * gammainc(o2nu, U)  - onu * power(U, -onu) * gamma(onu) * gammainc(onu, U)

	# Interbranch term
    N2 = 2.0*n
    U2 = q**2 * b**2 * power(N2, 2.0*nu) / 6.0
    P2p = onu * power(U2, -o2nu) * gamma(o2nu) * gammainc(o2nu, U2) - onu * power(U2, -onu) * gamma(onu) * gammainc(onu, U2)
    Pib = 2.0*P2p - Psb
	
    # Form the structure factor according to the RPA:
    Sq = 1.0/(f*f) * (f*Psb + f*(f-1.0)*Pib)
    inten = (sldp - slds) * (sldp - slds) * 1e-4 * Sq

    return inten

Iq.vectorized = True  # Iq accepts an array of q values


# Test/demo information for validation.
demo = dict(scale = 1, background = 0, sldp=1.0, slds=6.3, f=3, n=30, b=7, nu=0.5)

tests = [[0.005, 0.00380886618675],
         [0.5, 0.00103057414966]]