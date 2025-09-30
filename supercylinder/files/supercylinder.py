r"""
Definition
----------

.. image:: supercylinder_shapes.png
   :height: 150px
   :align: center

This supercylinder model is an implementation based on Maric *et al.*, 2017 [1]_ 
and may be used to calculate scattering from lipoproteins. 
The supercylinder shape can be described via a superellipsoid (Barr, 1992 [2]_) as:

.. math::

    \left(\left| x \right|^{2} + \left| y \right|^{2}\right)^{t/2} 
    + \left|\frac{z}{\epsilon}\right|^t \leq |R|^t

Setting $|r|^2 = \left| x \right|^{2} + \left| y \right|^{2}$, $r$ and $z$ can be related as:


.. math::

    r(z) = \left|R^t - \left|\frac{z}{\epsilon}\right|^t\right|^{1/t}

Where, $R$ is the radius at the equator, $\epsilon$ is the eccentricity and $t$ is 
the superellipticity.

.. image:: 2Dplot.png
    :height: 150px
    :width: 50%
    :align: center

In building the supercylinder model we use the form factor amplitude for a cylinder with length 
$2R\epsilon$ and radius $R$: 

.. math::

    F(q) = 2 \Delta \rho V \frac{\sin\left(\frac{1}{2} q
    (2 R\epsilon)\cos\theta\right) J_1\left(q R \sin\theta\right)}
    {\frac{1}{2}q (2R\epsilon) \cos\theta \ \ \ q R \sin\theta}

where $V$ is the volume of the supercylinder, $\Delta\rho$ is the contrast between the solvents 
and the particles scattering length density, and $J_1$ is the Bessel function of the first kind. 
If the radius is $R = r(z)$ such that it changes with $z$, we must integrate the all the small 
cylinders up over the length.

.. math::

    F(q) &= 2 \Delta \rho V \frac{\sin\left(q R\epsilon\cos\theta\right) 
    J_1\left(q R \sin\theta\right)}{q R\epsilon \cos\theta \ \ \ q R \sin\theta}\\
    &= 2 \int_0^{R \epsilon} 2 \Delta \rho \pi r(z)^2 \frac{J_1\left(q r(z) \sin\theta\right)}
    {q \cos\theta \ \ \ q r(z) \sin\theta} \cos\left(q z\cos\theta\right) q \cos\theta \ dz\\
    &=  \int_0^{R \epsilon} 4 \Delta \rho \pi r(z) \frac{J_1\left(q r(z) \sin\theta\right)}
    {q \sin\theta} \cos\left(q z\cos\theta\right) \ dz

Given randomly oriented particles, the form factor can be written as:

.. math::

    P(q) = \int^{\pi / 2}_0 \left| \int_0^{R\epsilon} 4 \Delta \rho \pi \epsilon r(z) 
    \frac{\cos\left( q  r(z)\cos\theta\right) J_1\left(q z\sin\theta\right)}{q \sin\theta} 
    \ dz \right|^2 \sin\theta \ d\theta

which is solved numerically. Thus, the supercylinder model is given as:

.. math::

    I(q) = \text{scale} \ P(q) + \text{background}


Validation
----------

The model is validated by using Shape2SAS (Larsen *et al.*, 2023 [3]_) 
to numerical generate SAXS for different supercylinders and fitting these with the model. 
It is found that the model describes the simulated data well.

.. image:: fit_50_2_3_2.png
    :height: 200px
    :width: 90%
    :align: center

References
----------

.. [1] Maric, Selma & Lind, Tania & Lyngsø, Jeppe & Cárdenas, Marité & Pedersen, Jan. (2017). Modeling Small-Angle X-Ray Scattering Data for Low Density Lipoproteins – Insights Into The Fatty Core Phase Packing And Transition. ACS Nano. 11. 10.1021/acsnano.6b08089. 
.. [2] A.H. Barr, III. 8-RIGID PHYSICALLY BASED SUPERQUADRICS, Editor(s): DAVID KIRK, Graphics Gems III (IBM Version), Morgan Kaufmann, 1992, Pages 137-159, ISBN 9780124096738, https://doi.org/10.1016/B978-0-08-050755-2.50038-5.
.. [3] Larsen A.H, Brookes E, Pedersen M.C, Kirkensgaard J.J.K. Shape2SAS -- a web application to simulate small-angle scattering data and pair distance distributions from user-defined shapes. ArXiv [Preprint]. 2023 Jan 12:arXiv:2301.04976v1. Update in: J Appl Crystallogr. 2023 Jul 28;56(Pt 4):1287-1294. PMID: 36713243; PMCID: PMC9882588.

Authorship and Verification
----------------------------

* **Author:** Thomas B. Hansen
* **Last Modified by:** Thomas B. Hansen
* **Last Reviewed by:** Thomas B. Hanse **Date:** 08/05/2024
"""

import numpy as np
from scipy.integrate import quad_vec
from scipy.special import j1

name = "supercylinder"
title = 'Supercylinder with uniform scattering length density'
description = """
    P(q) = scale * \int^{\pi / 2}_0 \left| \int_0^{R\epsilon} 4 (sld - sld_solvent) 
    \pi \epsilon r(z) \frac{\cos\left( q  r(z)\cos\theta\right) 
    J_1\left(q z\sin\theta\right)}{q \sin\theta} \ dz \right|^2 
    * \sin\theta \ d\theta + background
    
    sld: the scattering length density of the superellipsoid
    sld_solvent: the scattering length density of the solvent
    R: radius of the superellipsoid
    \epsilon: eccentricity of the superellipsoid
    t: shape exponent of the superellipsoid
"""

category = "shape:cylinder"
single = True
opencl = False

structure_factor = False

#             ["name", "units", default, [lower, upper], "type","description"],
parameters = [["sld", "10-6Å-2", 4, [0, np.inf], "", "lipoprotein scattering length density"],
              ["sld_solvent", "10-6Å-2", 1, [0, np.inf], "", "Solvent scattering length density"],
              ["R", "Å", 50, [0, np.inf], "", "The radius of the superellipsoid"],
              ["eps", "", 2, [0, np.inf], "", "eccentricity of the superellipsoid"],
              ["t", "", 3, [0, np.inf], "", "shape exponent of the superellipsoid"]
             ]


def r(z, R, eps, t):
    return (np.abs(R)**t - np.abs(z / eps)**t)**(1/t)


def inner_integrand(theta, q, R, eps, t, tol):
    inner = lambda z: (r(z, R, eps, t)
                * j1(q * r(z, R, eps, t) * np.sin(theta))
                * np.cos(q * z * np.cos(theta)))
    
    inner_res = (1 / np.sin(theta) * quad_vec(inner, 0,
                R * eps, epsabs=tol, epsrel=tol, quadrature="gk15")[0])**2
    
    return inner_res


def Iq(q, sld, sld_solvent, R, eps, t, tol):

    inner = lambda theta: inner_integrand(theta, q, R, eps, t, tol) * np.sin(theta)
    P = quad_vec(inner, 0, np.pi / 2, epsabs=tol, epsrel=tol, quadrature="gk15")[0]

    return P * (4 * (sld - sld_solvent) * np.pi / q)**2


Iq.vectorized = True


tests = [
     [{}, [0.1, 0.2, 0.3, 0.4, 0.5], [4.15571325e+10, 1.43440871e+09,
            6.00644471e+08, 8.24624104e+07, 7.17101120e+07]],
     [{'eps': 1., 't': 7.}, [0.1, 0.2, 0.3, 0.4, 0.5],
      [3.81807309e+10, 6.05532290e+08, 5.11919070e+08, 5.42343458e+07, 4.60311610e+07]],
     [{"@S": "hardsphere"}, 0.1, None]
]

