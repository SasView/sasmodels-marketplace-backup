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
#  Orientationally averaged form factor for a monodisperse spherical particle with a core-shell sphere structure, filled with a circular cylinder in its center.
#
#  (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#  (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#  (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#  (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#  (((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%(((((((((((((((((((((((((((((((
#  ((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%((((((((((((((((((((((((((
#  ((((((((((((((((((((((%%%%%%%%%%...............%%%%%%%%%%((((((((((((((((((((((
#  (((((((((((((((((((%%%%%%%%.........................%%%%%%%%(((((((((((((((((((
#  (((((((((((((((((%%%%%%.................................%%%%%%(((((((((((((((((
#  (((((((((((((((%%%%%%.....................................%%%%%%(((((((((((((((
#  ((((((((((((((%%%%%.........................................%%%%%((((((((((((((
#  ((((((((((((%%%%%.............................................%%%%%((((((((((((
#  (((((((((((%%%%%...%%%.........................................%%%%%(((((((((((
#  ((((((((((%%%%%...%%%%%%%%%.....................................%%%%%((((((((((
#  (((((((((%%%%%...%%%%%%%%%%%%%%%.................................%%%%%(((((((((
#  (((((((((%%%%....%%%%%%%%%%%%%%%%%%%%.............................%%%%(((((((((
#  ((((((((%%%%....%%%%%%%%%%%%%%%%%%%%%%%%%%%........................%%%%((((((((
#  ((((((((%%%%...%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...................%%%%((((((((
#  ((((((((%%%%..%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%..............%%%%((((((((
#  (((((((%%%%...%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%..........%%%%(((((((
#  (((((((%%%%........%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.....%%%%(((((((
#  ((((((((%%%%............%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...%%%%((((((((
#  ((((((((%%%%.................%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...%%%%((((((((
#  ((((((((%%%%......................%%%%%%%%%%%%%%%%%%%%%%%%%%%%%....%%%%((((((((
#  (((((((((%%%%..........................%%%%%%%%%%%%%%%%%%%%%%%....%%%%(((((((((
#  (((((((((%%%%%..............................%%%%%%%%%%%%%%%%%....%%%%%(((((((((
#  ((((((((((%%%%%..................................%%%%%%%%%%%....%%%%%((((((((((
#  (((((((((((%%%%%......................................%%%%%%...%%%%%(((((((((((
#  ((((((((((((%%%%%.............................................%%%%%((((((((((((
#  ((((((((((((((%%%%%.........................................%%%%%((((((((((((((
#  (((((((((((((((%%%%%%.....................................%%%%%%(((((((((((((((
#  (((((((((((((((((%%%%%%.................................%%%%%%(((((((((((((((((
#  (((((((((((((((((((%%%%%%%%.........................%%%%%%%%(((((((((((((((((((
#  ((((((((((((((((((((((%%%%%%%%%%...............%%%%%%%%%%((((((((((((((((((((((
#  ((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%((((((((((((((((((((((((((
#  (((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%(((((((((((((((((((((((((((((((
#  (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#  (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#  (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
r"""
Definition
----------

Parameters:
    scale = scaling factor, volume fraction of particles scale phi ~ N V_{sph} / V_{irr}, with N / V_{irr} being the number density of particles in the irradiated volume
    background = const. background
    R_{sph,c} = core radius of sphere
    d_{sph,sh} = shell thickness of sphere
    NB: R_{sph,c} + d_{sph,sh} = radius of whole sphere
    R_{cyl} = radius of cylinder
    L_{cyl} = length of cylinder
    V_{sph} = volume of whole sphere including shell
    V_{sph,c} = volume of sphere core
    V_{cyl} = volume of cylinder
    sld_{sph,c} = scattering length density of core of sphere
    sld_{sph,sh} = scattering length density of shell of sphere
    sld_{cyl} = scattering length density of cylinder inside the core
    sld_{solv} = scattering length density of solvent


For the particles with a non-spherical symmetry an orientational average is applied:

    F^2(q) = int_{0}^{pi/2} f^2(q,alpha) sin(alpha) dalpha

The output of the 1D scattering intensity function is then given by

    P(q) = frac{	ext{scale}}{V_{sph}} int_0^{pi/2} f^2(q,alpha) sinalpha dalpha + 	ext{background}

where

    f(q,alpha) = ( sld_{cyl}-sld_{sph,c} ) * V_{cyl} f_cyl(q,alpha) 
               + ( sld_{sph,c}-sld_{sph,sh} ) * V_{sph,c} f_sph( q*R_{sph,c} ) 
               + ( sld_{sph,sh}-sld_{solv} ) * V_{sph} f_sph( q*(R_{sph,c}+d_{sph,sh}) )

where

    f_cyl(q,alpha) = j_0( q*L_{cyl}*cos(alpha)/2 ) * 2J1x( q*R_{cyl}sin(alpha) )
    f_sph(x) = 3 * frac{ sin(x)-xcos(x) }{ x^3 }

where

    j_0(x) = sin(x) / x
    2J1x(x) = 2 * J_1(x) / x , where $J_1$ is the first order Bessel function
    V_{cyl} = pi R_{cyl}^2 L_{cyl}
    V_{sph,c} = 4pi/3 R_{sph,c}^3
    V_{sph} = 4pi/3 (R_{sph,c}+d_{sph,sh})^3


For 2D:

The $cyl_orient_theta$ and $cyl_orient_phi$ parameters only appear in the model when fitting 2D data. For oriented cylinders, we define the direction of the axis of the cylinder using two angles $cyl_orient_theta$ and $cyl_orient_phi$. See cylinder angle definition:

.. figure:: img/cylinder_angle_definition.jpg



Validation
----------

Checked at different contrast conditions if it matches P(Q) of a (core-shell) sphere or a cylinder.


References
----------

Cylinders:
J. S. Pedersen, Adv. Colloid Interface Sci. 70, 171-210 (1997).
G. Fournet, Bull. Soc. Fr. Mineral. Cristallogr. 74, 39-113 (1951).
"""

import numpy as np  # type: ignore
from numpy import pi, inf  # type: ignore

name = "coreshellspherecylinder"
title = "Orientationally averaged form factor for a monodisperse spherical particle with a core-shell sphere structure, filled with a circular cylinder in its center."
description = """
Output:
    P(q) = frac{	ext{scale}}{V_{sph}} int_0^{pi/2} f^2(q,alpha) sinalpha dalpha + 	ext{background}

where
    f(q,alpha) = ( sld_{cyl}-sld_{sph,c} ) * V_{cyl} f_cyl(q,alpha) 
               + ( sld_{sph,c}-sld_{sph,sh} ) * V_{sph,c} f_sph( q*R_{sph,c} ) 
               + ( sld_{sph,sh}-sld_{solv} ) * V_{sph} f_sph( q*(R_{sph,c}+d_{sph,sh}) )

where
    f_cyl(q,alpha) = j_0( q*L_{cyl}*cos(alpha)/2 ) * 2J1x( q*R_{cyl}sin(alpha) )
    f_sph(x) = 3 * frac{ sin(x)-xcos(x) }{ x^3 }

where
    j_0(x) = sin(x) / x
    2J1x(x) = 2 * J_1(x) / x , where $J_1$ is the first order Bessel function
    V_{cyl} = pi R_{cyl}^2 L_{cyl}
    V_{sph,c} = 4pi/3 R_{sph,c}^3
    V_{sph} = 4pi/3 (R_{sph,c}+d_{sph,sh})^3

Parameters:
    scale = scaling factor, volume fraction of particles scale phi ~ N V_{sph} / V_{irr}, with N / V_{irr} being the number density of particles in the irradiated volume
    background = const. background
    R_{sph,c} = core radius of sphere
    d_{sph,sh} = shell thickness of sphere
    NB: R_{sph,c} + d_{sph,sh} = radius of whole sphere
    R_{cyl} = radius of cylinder
    L_{cyl} = length of cylinder
    V_{sph} = volume of whole sphere including shell
    V_{sph,c} = volume of sphere core
    V_{cyl} = volume of cylinder
    sld_{sph,c} = scattering length density of core of sphere
    sld_{sph,sh} = scattering length density of shell of sphere
    sld_{cyl} = scattering length density of cylinder inside the core
    sld_{solv} = scattering length density of solvent
"""
category = "shape:cylinder"

#           [ "name", "units", default, [lower, upper], "type", "description"],
#
# convention, first SLDs, then geometry, then orientation
# all functions in C and dict(demo) entries in Py should follow this convention, in order to not mix up params
parameters = [
              ["sld_core", "1e-6/Ang^2", 0.0, [-inf, inf], "sld", "core scattering length density"],
              ["sld_shell", "1e-6/Ang^2", 4.0, [-inf, inf], "sld", "shell scattering length density"],
              ["sld_cyl", "1e-6/Ang^2", 4.0, [-inf, inf], "sld", "cylinder scattering length density"],
              ["sld_solvent", "1e-6/Ang^2", 6.34, [-inf, inf], "sld", "solvent scattering length density"],
              ["sphere_core_radius", "Ang", 500.0, [0, inf], "volume", "sphere core radius"],
              ["sphere_shell_thickness", "Ang", 100.0, [0, inf], "volume", "sphere shell thickness"],
              ["cyl_radius", "Ang", 400.0, [0, inf], "volume", "cylinder radius"],
              ["cyl_length", "Ang", 250.0, [0, inf], "volume", "cylinder length"],
              ["cyl_orient_theta", "degrees", 60, [-inf, inf], "orientation", "latitude"],
              ["cyl_orient_phi", "degrees", 60, [-inf, inf], "orientation", "longitude"]]

source = ["lib/sas_3j1x_x.c", "lib/polevl.c", "lib/sas_J1.c", "lib/gauss76.c", "coreshellspherefilledwithcylinder.c"]


# cylinder
# NB: The 2nd virial coefficient of the cylinder is calculated based on the radius and length values, and used as the effective radius for $S(q)$ when $P(q) cdot S(q)$ is applied.
#
#def ER(radius, length):
#  """
#      Return equivalent radius (ER)
#  """
#  ddd = 0.75 * radius * (2 * radius * length + (length + radius) * (length + pi * radius))
#  return 0.5 * (ddd) ** (1. / 3.)


# core-shell sphere
# NB: The outer most radius (ie, = radius + thickness) is used as the effective radius for $S(Q)$ when $P(Q) cdot S(Q)$ is applied.
# 
def ER(sphere_core_radius, sphere_shell_thickness):
    """
        Equivalent radius
        @param sphere_core_radius: sphere core radius
        @param sphere_shell_thickness: sphere shell thickness
    """
    return sphere_core_radius + sphere_shell_thickness


# core-shell sphere
#def VR(radius, thickness):
#  """
#      Volume ratio
#      @param radius: core radius
#      @param thickness: shell thickness
#  """
#  return (1, 1)
#  whole = 4.0/3.0 * pi * (radius + thickness)**3
#  core = 4.0/3.0 * pi * radius**3
#  return whole, whole - core



# parameters for demo
demo = dict(scale=1,
            background=0,
            sld_core=0.0,
            sld_shell=4.0,
            sld_cyl=4.0,
            sld_solvent=6.34,
            sphere_core_radius=500,
            sphere_shell_thickness=100,
            cyl_radius=400,
            cyl_length=250,
            cyl_orient_theta=60,
            cyl_orient_phi=60
)
#            cyl_radius_pd=.2, cyl_radius_pd_n=9,
#            cyl_length_pd=.2, cyl_length_pd_n=10,



qx, qy = 0.2 * np.cos(2.5), 0.2 * np.sin(2.5)
# After redefinition of angles, find new tests values.  Was 10 10 in old coords
tests = [[{}, 0.2, 0.042761386790780453],
        [{}, [0.2], [0.042761386790780453]],
#  new coords    
        [{'cyl_orient_theta':80.1534480601659, 'cyl_orient_phi':10.1510817110481}, (qx, qy), 0.03514647218513852],
        [{'cyl_orient_theta':80.1534480601659, 'cyl_orient_phi':10.1510817110481}, [(qx, qy)], [0.03514647218513852]],
# old coords   [{'cyl_orient_theta':10.0, 'cyl_orient_phi':10.0}, (qx, qy), 0.03514647218513852],
#            [{'cyl_orient_theta':10.0, 'cyl_orient_phi':10.0}, [(qx, qy)], [0.03514647218513852]],
        ]
del qx, qy  # not necessary to delete, but cleaner

