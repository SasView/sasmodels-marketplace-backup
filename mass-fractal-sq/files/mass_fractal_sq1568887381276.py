r"""

Calculates the structure factor term ONLY from the Mass Fractal model.

Definition
----------
The functional form of the structure factor is defined below.

.. math::

    S(q) = frac{Gamma(D_m-1)xi^{D_m-1}}{left[1+(qxi)^2
    ight]^{(D_m-1)/2}}
    frac{sinleft[(D_m - 1) tan^{-1}(qxi) ight]}{q}

where $D_m$ is the **mass** fractal dimension and $xi$ is the upper fractal cutoff
length i.e. the length scale above which the system is no longer fractal.

SasView automatically appends two additional parameters $radius_effective$ and
$volfraction$ to all $S(q)$ models. However, these are not used by this model.

.. note::

    The mass fractal dimension ( $D_m$ ) is only valid if $1 <= D_m <= 3$.
	It is also only valid over a limited $q$ range (see the references for details).

.. note::

    WARNING! By convention, $S(q)$ is normally dimensionless.
	**This function is not dimensionless**.

References
----------

D Mildner and P Hall, *J. Phys. D: Appl. Phys.*,
19 (1986) 1535-1545 Equation(9)

P Wong, *Methods in the physics of porous media*
San Diego; London. Academic. (1999) 

Authorship and Verification
----------------------------

* **Author:** Ziggy Attala and Matt D G Hughes **Date:** 09/09/2019
* **Last Modified by:** Steve King **Date:** 18/09/2019
* **Last Reviewed by:** **Date:**

"""
import numpy as np
from numpy import inf

name = "mass_fractal_sq"
title = "Mass Fractal Structure Factor"
description = """Calculates the structure
 factor term ONLY from
 the Mass Fractal model.
"""
category = "structure-factor"
structure_factor = True
single = False

parameters = [["radius_effective", "Ang", 50.0, [0, inf], "",
               "effective radius of hard sphere"],
              ["volfraction", "", 0.0, [0, 0.74], "",
               "volume fraction of hard spheres"],
              ["cutoff_length", "Ang", 150.0, [0, inf], "",
			   "Cutoff length of fractal"],
              ["fractal_dimension", "", 2.1, [1, 3], "",
			   "Mass fractal dimension"]]

source = ["libsas_gamma.c"]

Iq = r"""
    double x = q;

    double term_1, term_2;
    double term_1_numerator, term_1_denominator;
    double term_2_numerator;
    // Only used in this function as (fractal_dimension -1).
    double _fractal_dimension = fractal_dimension - 1;

    term_1_numerator = pow(cutoff_length, _fractal_dimension) * sas_gamma(_fractal_dimension);
    double _pow = _fractal_dimension / 2;
    term_1_denominator = pow(1 + square(x * cutoff_length), _pow);
    term_1 = term_1_numerator / term_1_denominator;

    term_2_numerator = sin(_fractal_dimension * atan(x * cutoff_length));
    term_2 = term_2_numerator / x;

    double sq = term_1 * term_2;
    return(sq);
"""

tests  = [[{'scale': 1.0, 'background' : 0.0, 'cutoff_length' : 250.0, 'fractal_dimension' : 2.0},
           [0.001, 0.5], [61538.461538461546, 3.999744016382952]]
    ]