r"""

Flexible exponential model with a flat background.

Definition
----------
This model calculates a variety of exponential functions.

The scattered intensity $I(q)$ is calculated as

.. math::

    I(q) = 	ext{scale} cdot exp(-	ext{prefactor} cdot (q^{	ext{exponent}}) + 	ext{background}

Note the minus sign in the exponential term. Thus if *prefactor* is entered
as a **positive number** during fitting the returned function will decrease
as *q* increases.

Also note that unlike many other models, *scale* in this model is NOT
explicitly related to a volume fraction. Be careful if combining this model
with other models.

The value of *exponent* controls the behaviour of the function. When:

*exponent*=1   : a **normal exponential** function is returned

0<*exponent*<1 : a so-called **stretched exponential** (or Kohlrausch-Williams-
                 Watts, KWW) [1,2] function is returned

*exponent*>1   : a **compressed exponential** is returned

*exponent*=2   : a **normal distribution** function is returned.

This model probably has limited applicability in the analysis of SAS data but
is of great use in allied fields. For example, the KWW function is used in the
analysis of dielectric spectra data, rheological relaxation data, and dynamic
light scattering (photon correlation spectroscopy) data.

References
----------

#.  R. Kohlrausch, *Annalen der Physik und Chemie* 91(1) (1854) 56-82, 179-213 
#.  G. Williams & D.C. Watts *Transactions of the Faraday Society* 66 (1970) 80-85

Authorship and Verification
---------------------------

* **Author:** Steve King **Date:** 07/03/2020
* **Last Modified by:** **Date:**
* **Last Reviewed by:** **Date:**

"""
import numpy as np
from numpy import inf

name = "exponential"
title = "Exponential model"
description = """
    Evaluates the function
    I(q) = scale .
	exp(-prefactor . (q^exponent))
	+ bkgd
"""
category = "shape-independent"
structure_factor = False
single = False

#   ["name", "units", default, [lower, upper], "type","description"],
parameters = [
    ["prefactor", "", 1.0, [-inf, inf], "", "Prefactor"],
    ["exponent", "", 1.0, [-inf, inf], "", "Exponent"],
]

def Iq(q, prefactor, exponent):
    result = np.exp(-1.0*prefactor*np.power(q,exponent))
    return result
	
Iq.vectorized = True  # Iq accepts an array of q values

tests = [
    [{'scale': 1.0, 'background' : 0.001, 'prefactor' : 2.0,
      'exponent' : 0.5},
     [0.0005, 0.5], [0.957263898517, 0.244116734434]],
	]
