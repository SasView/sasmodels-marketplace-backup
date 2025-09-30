#  Author: 
#    Martin Schmiele
#    Niels-Bohr-Institutet
#    Koebenhavns Universitet
#    martin.schmiele@nbi.ku.dk
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#
#  Orientationally averaged form factor for a monodisperse core-shell cuboid.
#
#               ,p=.,,_                   
#             ,/l:]:::::77t==.,,_          
#          ,/5::::[::::::::::::::773==.,,_ 
#       ,/5:::::::{zps;;:::::::::::::::::ZL
#    ,/5::::::::;z$3EtttZZ5sws;;:::::::yEJ.
# ,/5:::::::::zEtt$3EtttttttttttZZQ@:yE::[ 
# J=775es;;;Z5tttt3EEtttttttttttt@E@/::::L 
#  L::::::@8N@@szj3EEtttttttttt@E3@E::::3L 
#  {::::::$ttttZ59Q@BgszjttttgE1ZZ3E::::{  
#  J::::::Jttttttt3EEZZ55B@@SE2K5t3L::::[  
#   L:::::JEttttt25E35Sz@zz$ttQttt$:::::L  
#   [::::::Ettt25EttttttttZV5U$szj$::::J.  
#   J::::::$t25Ettttttttttt$t31tt2Pwsz;]   
#    L:::::@5EtttttttttttttEt3[zZ:::::y`   
#    [:::/5?3Gszjtttttttttt$tJ@E:::::/     
#    J;z5:::::::775szjtttttEz@L:::::F      
#     *+z;::::::::::::73Gsg@EJ.:::yF       
#         `*+z;::::::::::::::{:::/`        
#              `*=z;:::::::::[::F          
#                   `*=c;::::[yF           
#                        `*=cE`            
#
r"""
Definition
----------

Parameters:
    scale = scaling factor, volume fraction of particles scale phi ~ N V_{cs} / V_{irr}, with N / V_{irr} being the number density of particles in the irradiated volume
    background = const. background
    L = length of the cuboid
    d = shell thickness
    ho_{c} = scattering length density of core
    ho_{sh} = scattering length density of shell
    ho_{solv} = scattering length density of solvent
    V_{cs} = volume of core-shell cuboid

For the particles with a non-spherical symmetry an orientational average is applied:

    F^2(q) = int_{0}^{pi}int_{0}^{2pi} f^2(q,	heta_Q,phi_Q) sin(	heta_Q) d	heta_Q dphi_Q

The output of the 1D scattering intensity function is then given by

    P(q) = frac{	ext{scale}}{V_{cs}} F^2(q) + 	ext{background}

where
    f(q,	heta_Q,phi_Q) = ( ho_{c}-ho_{sh} ) prod_{j=1}^3 [ 2 * L/2 * sinc(Q_j*L/2) ] + ( ho_{sh}-ho_{solv} ) * prod_{j=1}^3 [ 2 * (L/2+d) * sinc(Q_j*(L/2+d)) ]

where
    sinc(x) = sin(x) / x

    Q_1 = Q sin(	heta_Q) cos(phi_Q)
    Q_2 = Q sin(	heta_Q) sin(phi_Q)
    Q_3 = Q cos(	heta_Q)



For 2D:

To provide easy access to the orientation of the parallelepiped, we define the axis of the cylinder using three angles $	heta$, $phi$ and $psi$.
(see :ref:`cylinder orientation <cylinder-angle-definition>`).

  figure:: img/parallelepiped_angle_definition.jpg

    Definition of the angles for oriented core-shell parallelepipeds.

  figure:: img/parallelepiped_angle_projection.jpg

    Examples of the angles for oriented core-shell parallelepipeds against the detector plane.


Validation
----------
    Compared with core-shell sphere using same core diameter (700 AA) and shell thickness (150 AA) and same SLDs provides same patterns at mid and high Q when using 25% Gaussian PDs for core radius/diameter and shell thickness



References
----------
    P Mittelbach and G Porod, *Acta Physica Austriaca*, 14 (1961) 185-211 Equations (1), (13-14). (in German)
    D Singh (2009). *Small angle scattering studies of self assembly in lipid mixtures*, John's Hopkins University Thesis (2009) 223-225.

"""

import numpy as np
from numpy import pi, inf, sqrt

name = "core_shell_cuboid"
title = "Orientationally averaged form factor for a monodisperse core-shell cuboid."
description = """
Output:
    P(q) = frac{	ext{scale}}{V_{cs}} int_{0}^{pi}int_{0}^{2pi} f^2(q,	heta_Q,phi_Q) sin(	heta_Q) d	heta_Q dphi_Q + 	ext{background}

where
    f(q,	heta_Q,phi_Q) = ( ho_{c}-ho_{sh} ) prod_{j=1}^3 [ 2 * L/2 * sinc(Q_j*L/2) ] + ( ho_{sh}-ho_{solv} ) * prod_{j=1}^3 [ 2 * (L/2+d) * sinc(Q_j*(L/2+d)) ]

where
    sinc(x) = sin(x) / x

    Q_1 = Q sin(	heta_Q) cos(phi_Q)
    Q_2 = Q sin(	heta_Q) sin(phi_Q)
    Q_3 = Q cos(	heta_Q)

Parameters:
    scale = scaling factor, volume fraction of particles scale phi ~ N V_{cs} / V_{irr}, with N / V_{irr} being the number density of particles in the irradiated volume
    background = const. background
    L = length of the cuboid
    d = shell thickness
    ho_{c} = scattering length density of core
    ho_{sh} = scattering length density of shell
    ho_{solv} = scattering length density of solvent
    V_{cs} = volume of core-shell cuboid
"""
category = "shape:parallelepiped"

#             ["name", "units", default, [lower, upper], "type","description"],
parameters = [["sld_core", "1e-6/Ang^2", 1, [-inf, inf], "sld", "Cuboid core scattering length density"],
              ["sld_shell", "1e-6/Ang^2", 2, [-inf, inf], "sld", "Cuboid shell scattering length density"],
              ["sld_solvent", "1e-6/Ang^2", 6.34, [-inf, inf], "sld", "Solvent scattering length density"],
              ["length", "Ang", 700, [0, inf], "volume", "Length of the Cuboid core"],
              ["thick_rim", "Ang", 150, [0, inf], "volume", "Thickness of the shell"],
              ["theta", "degrees", 0, [-inf, inf], "orientation", "In plane angle"],
              ["phi", "degrees", 0, [-inf, inf], "orientation", "Out of plane angle"],
              ["psi", "degrees", 0, [-inf, inf], "orientation", "Rotation angle around its own c axis against q plane"]]

source = ["lib/gauss76.c", "core_shell_cuboid.c"]


# NB: use effective radius for $S(q)$ when $P(q) cdot S(q)$ is applied.
def ER(length, thick_rim):
    """
        Return equivalent radius (ER)
    """
    total_length = length + 2.0 * thick_rim 

    # # approximation using 2nd virial coeff for a cylinder with surface average radius (rough approximation)
    # # surf_rad = sqrt( total_length * total_length ) / pi
    # surf_rad = total_length / pi
    # height = total_length
    # ddd = 0.75 * surf_rad * (2 * surf_rad * height + (height + surf_rad) * (height + pi * surf_rad))
    # # ER would be approx. 2/5 * total_length ( (3/32/pi*(1+4/pi))^(1/3) == 0.40784 )
    # return 0.5 * (ddd) ** (1./3.)

    # use approximation of volume averaged radius (same volume of sphere and cuboid), might be better as the approximation with cylinder since for cuboid a=b=c
    # ER = ( V / ( 4. * pi / 3.) ) ** (1./3.) where V = total_length**3. and (3/4/pi)^(1/3) == 0.62035
    ER = total_length * ( 3. / ( 4. * pi ) ) ** (1./3.)



# VR defaults to 1.0



# parameters for demo
demo = dict(scale=1,
            background=0.0,
            sld_core=1,
            sld_shell=2,
            sld_solvent=6.34,
            length=700,
            thick_rim=150,
            theta=0,
            phi=0,
            psi=0
)
#            length_pd=0.1, length_pd_n=1,
#            thick_rim_pd=0.1, thick_rim_pd_n=1,
#            theta_pd=10, theta_pd_n=1,
#            phi_pd=10, phi_pd_n=1,
#            psi_pd=10, psi_pd_n=1


qx, qy = 0.2 * np.cos(2.5), 0.2 * np.sin(2.5)
tests = [[{}, 0.2, 0.533149288477],
         [{}, [0.2], [0.533149288477]],
         [{'theta':10.0, 'phi':10.0}, (qx, qy), 0.032102135569],
         [{'theta':10.0, 'phi':10.0}, [(qx, qy)], [0.032102135569]],
        ]
del qx, qy  # not necessary to delete, but cleaner
