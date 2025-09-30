r"""
The Benoit model for a simple star polymer, with Gaussian coils arms from
a common point.
[TEST new version May 2017, fit Rg not (Rg)^2, start to check results at very small Q,
see tickets #552 & #962 ]

Definition
----------

For a star with $f$ arms the scattering intensity $I(q)$ is calculated as

.. math::

    I(q) = frac{2}{fv^2}left[ v-1+exp(-v)+frac{f-1}{2}
           left[ 1-exp(-v)ight]^2ight]

where

.. math:: v=frac{u^2f}{(3f-2)}

and

.. math:: u = leftlangle R_{g}ightangle q^2

Rg is the radius-of-gyration of the whole star.
Note that when there is only one arm, $f = 1$, the Debye Gaussian coil
equation is recovered. Star polymers in solutions tend to have strong
interparticle and osmotic effects, so the Benoit equation may not work well.
See discussions in literature, such as Willner et.al.

At small $q$ the Guinier term and hence $I(q=0)$ is the same as for $f$ arms
of radius of gyration $R_g$, as described for the :ref:`mono-gauss-coil` model.

References
----------

H Benoit *J. Polymer Science*, 11, 596-599 (1953)

L.Willner, O.Jucknischke, D.Richter, J.Roovers, L.-L. Zhou, P.M.Toporowski,
L.J.Fetters, J.S.Huang, M.Y.Lin & N.Hadjichristidis, Macromolecules 27, 3821-3829 (1994)
"""

from numpy import inf

name = "star_polymer_v2"
title = "Star polymer model with Gaussian statistics"
description = """
        Benoit 'Star polymer with Gaussian statistics'
        with
        P(q) = 2/{fv^2} * (v - (1-exp(-v)) + {f-1}/2 * (1-exp(-v))^2)
        where
        - v = u.f/(3f-2)
        - u = <R_g^2>q^2, where <R_g^2> is the ensemble average radius of
        gyration of the whole star
        - f is the number of arms in the star
        """
category = "shape-independent"
single = False
# pylint: disable=bad-whitespace, line-too-long
#             ["name", "units", default, [lower, upper], "type","description"],
parameters = [["rg", "Ang^2", 10.0, [0.0, inf], "", "radius of gyration of star"],
              ["arms",    "",      3,   [1.0, 6.0], "", "Number of arms in the star"],
             ]
# pylint: enable=bad-whitespace, line-too-long

source = ["star_polymer_v2.c"]

demo = dict(scale=1, background=0,
            rg= 10.0,
            arms=3.0)

tests = [[{'rg': 1.414213562,
           'arms':    3.3,
          }, 0.5, 0.851646091108],

         [{'rg':    1.0,
           'arms':       2.0,
           'background': 1.8,
          }, 1.0, 2.53575888234],
        ]
# 23Mar2016  RKH edited docs, would this better use rg not rg^2 ? Numerical noise at extremely small q.rg
# 22May2017 RKH starts version2
