r"""

Calculates the structure factor term ONLY from the Fractal model.

Definition
----------
The Teixeira & Chen fractal structure factor.

Calculates the structure factor for mass fractal aggregates of monodisperse
spherical particles of effective radius $R_p$ according to

..math::
                S(q) = 1 + frac{D_mGamma(D_m - 1)}{(qR_p)^{D_m}
                [1+(qxi)^{-2}]^{(D_m-1)/2}} sin[(D_m - 1) tan^{-1}(qxi)]

                S(q) &= 1 + frac{D_f  Gamma!(D_f-1)}{[1+1/(q xi)^2  ]^{(D_f -1)/2}}
                frac{sin[(D_f-1) 	an^{-1}(q xi) ]}{(q R_0)^{D_f}}

where $D_m$ is the mass fractal dimension, $R_p$ is assumed to be
equivalent to the lower fractal cutoff length, and $xi$ is the upper fractal
cutoff length (the distance above which the mass distribution of the fractal
no longer scales as (size)^D_m).

The returned value is a dimensionless structure factor, $S(q)$.

The radius-of-gyration for the mass fractal is given by

..math::

                R_g = frac{D_m(D_m + 1)xi^{2}}{2}

Unlike most other structure factor models, this $S(q)$ does not explicitly
include the particle volume fraction and so the $volfraction$ parameter that
SasView adds by default has no effect. If combining this model with a
particulate form factor, use the $scale$ parameter to adjust the effective
volume fraction.

Combining this structure factor model with either the Sphere model or the
Core_Shell_Sphere model replicates the Fractal model or the
Fractal_Core_Shell model, respectively. In the latter case, make
$radius$_$effective$ = $radius$ + $thickness$.

.. note::

      The mass fractal dimension, which can be fractional, is only valid in the
	  range $1 <= D_m <= 3$. The S(q) function here goes negative if $D_m$ is 
	  too large, and the Gamma function diverges at $D_m$ = 0 and $D_m$ = 1.

References
----------

J Teixeira, *J. Appl. Cryst.*, 21 (1988) 781-785

Chapter 6, Equation 6.51 in
*Small-Angle Scattering from Confined and Interfacial Fluids*
Yuri B. Melnichenko
Springer, 2016

Authorship and Verification
---------------------------

* **Author:** Ziggy Attala **Date:** 10/09/2019
* **Last Modified by:** Steve King **Date:** 19/09/2019
* **Last Reviewed by:** **Date:**

"""
import numpy as np
from numpy import inf

name = "fractal_sq"
title = "Fractal Structure Factor"
description = """
 Calculates the structure
 factor term ONLY from
 the Fractal model.
 The Teixeira & Chen
 fractal structure factor.

 volfraction is not used
 by this model.
"""
category = "structure-factor"
structure_factor = True
single = False

parameters = [["radius_effective", "Ang", 50.0, [0, inf], "",
               "Effective radius of hard sphere"],
              ["volfraction", "", 0.0, [0, 0.74], "",
               "Volume fraction of hard spheres"],
              ["cutoff_length", "Ang", 150.0, [0, inf], "",
			   "Upper fractal cutoff length"],
              ["fractal_dimension", "", 2.1, [1, 3], "",
			   "Mass fractal dimension"]]

source = ["libsas_gamma.c"]

Iq = r"""
	double x = q;
	double dm = fractal_dimension;
	double c = cutoff_length;
	double r = radius_effective;
	
    double term_1, term_2;
	double term_1_numerator, term_1_denominator;
	double term_2_inner;
	
	term_1_numerator = dm * sas_gamma(dm - 1);
	term_1_denominator = pow((x * r), dm) * pow((1 + pow((x * c), -2)), (dm - 1)/2);
	
	term_1 = term_1_numerator / term_1_denominator;
	
	term_2_inner = (dm - 1) * atan(x * c);
	term_2 = sin(term_2_inner);
	
	double sq = 1 + (term_1 * term_2);
	return(sq);
"""

tests  = [[{'scale': 1.0, 'background' : 0.0, 'radius_effective' : 5.0,
            'cutoff_length' : 250.0, 'fractal_dimension' : 2.1},
           [0.001, 0.5], [7608.25508186, 1.28845539702]]
    ]