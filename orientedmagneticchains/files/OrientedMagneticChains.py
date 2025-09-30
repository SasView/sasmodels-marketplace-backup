r"""

Definition
----------
This plug-in model calculates oriented core-shell chains, with the option of 
adding a magnetic SLD to each layer. The chain scattering is the incoherent 
sum of a user-defined combination of singletons, dimers, trimers, 
quadramers, and pentamers. Note that no matter the numerical values 
selected for the amount of each chain type, the fraction of each will be 
normalized such that the sum of the chain type fractions is unity. A 
normalization radius parameter is also included that so that the scale will 
be equivalent to the volume fraction corresponding to that size of the 
nanoparticle (e.g. if the amount of iron oxide nanoparticle material in a 
solution is known, but the amount of surfactant is not, a normalization 
radius corresponding to the iron oxide radius will return a scale equal to 
the volume fraction of iron oxide in solution).

The chains are preferentially oriented about the x-direction, with a Gaussian 
FWHM in degrees set by user-input sigma. From here, the user can choose 
the viewing angle w.r.t. the x-axis (0 degrees and 90 degrees would be 
common slices). Alternatively, the user can select the 2D View before 
plotting the model to see a 2D plot; plotting 2D after starting a 1D plot may 
result in having the 1D plot determined by the viewing angle be symmetrically 
rotated about 2D, which would is not physically correct.

The magnetism of the chains comes in three varieties, selected using the 
parameter magnetic_orientation: 1 = core-shells with random magnetic 
alignment from particle-to-particle (but with a shared direction per core and 
shell), 2 = magnetic moments aligned along the chain axis, and 3 = magnetic 
moments aligned along the x-axis (regardless of chain orientation).
The scattering amplitude form factor is calculated in same way as the core-shell 
sphere model (Guinier, 1955), and it is then multiplied by a complex structure 
factor that depends on chain length:
.. math::
    P(q) = frac{	ext{scale}}{V} F^2(q)*(	ext{real  phase}^2 + 	ext{img  phase}^2) + 	ext{background}  
where
.. math::
    	ext{real  phase} =  1.0 + sum_{k=0}^{4} sum_{n=0}^{k} cos(k*length*(Q_X*cos(	heta) + Q_Y*sin(	heta)*cos(phi))
and
.. math::
    	ext{img  phase} =  0.0 + sum_{k=0}^{4} sum_{n=0}^{k} sin(k*length*(Q_X*cos(	heta) + Q_Y*sin(	heta)*cos(phi))
and
.. math::
    F(q) = frac{3}{V_s}left[
       V_c(ho_c-ho_s)frac{sin(qr_c)-qr_ccos(qr_c)}{(qr_c)^3} +
       V_s(ho_s-ho_	ext{solv})frac{sin(qr_s)-qr_scos(qr_s)}{(qr_s)^3}
       ight].

Here $V_s$ is the volume of the whole particle, $V_c$ is the volume of the
core, $r_s$ = $radius$ + $thickness$ is the radius of the particle, $r_c$
is the radius of the core, $ho_c$ is the scattering length density of the
core, $ho_s$ is the scattering length density of the shell,
$ho_	ext{solv}$, is the scattering length density of the solvent.

Theta is the angle between Qx-Qy and the x-axis, and it is sampled in 2 degree 
increments in 45 steps. Phi is the rotation of the vector set by theta in a 
half-cone about the x-axis in 4 steps of 45 degrees (finer steps are possible, but 
would slow the code and don't noticeably affect the model).

Please note, this model will soon be updated to include polarization analysis 
(currently unpolarized) and will include ability to change the orientation angle 
(now set to x). It will also include a fully randomly oriented option.

References
----------

#. A Guinier and G Fournet, *Small-Angle Scattering of X-Rays*,
   John Wiley and Sons, New York, (1955)

Authorship and Verification
----------------------------

* **Author:**
* **Last Modified by:**
* **Last Reviewed by:**
"""

import numpy as np
from sasmodels.special import *
from numpy import inf

name = "OrientedMagneticChains"
title = "Magnetic core-shell chains oriented about X-axis"
description = """User model for magnetic_coreshell_chains oriented about X-axis"""

category = "shape:sphere"

parameters = [["normalization_radius", "Ang", 50.0, [0, inf], "", "Radius of nanoparticle for which Scale = Volume Fraction"],
              ["sld_core", "1e-6/Ang^2", 6.9, [-inf, inf], "sld", "Layer scattering length density"],
              ["sld_magcore", "1e-6/Ang^2", 1.4, [-inf, inf], "sld", "Magnetic layer scattering length density"],
              ["sld_shell", "1e-6/Ang^2", 0.5, [-inf, inf], "", "Layer scattering length density"],
              ["sld_magshell", "1e-6/Ang^2", 0.0, [-inf, inf], "", "Magnetic layer scattering length density"],
              ["sld_solvent", "1e-6/Ang^2", 0.0, [-inf, inf], "sld", "Solvent scattering length density"],
              ["radius_core", "Ang", 50.0, [0, inf], "volume", "Sphere radius"],
              ["thickness_shell", "Ang", 10.0, [0, inf], "volume", "Shell thickness"],
              ['magnetic_orientation', '1=random;2=alongchain;3=alongfield', 2, [1, 3], '', ''],
              ['length', "Ang", 120.0, [0, inf], '', 'Particle center-to-particle center length'],
              ['viewing_angle', 'Angle w.r.t. x-axis (degrees)', 0, [0, 90], '', ''],
              ['sigma', 'Standard deviation of chain orientation about x (degrees)', 10, [0.5, 5000], '', ''],
              ['singlets', 'Fraction of singlets', 1.0, [0, 100], '', ''],
              ['doublets', 'Fraction of doubles', 1.0, [0, 100], '', ''],
              ['trimers', 'Fraction of trimers', 1.0, [0, 100], '', ''],
              ['quadramers', 'Fraction of quadramers', 1.0, [0, 100], '', ''],
              ['pentamers', 'Fraction of pentamers', 1.0, [0, 100], '', ''],
             ]

source = ["lib/sas_3j1x_x.c", "OrientedMagneticChains.c"]
have_Iq = True
have_Iqxy = True


