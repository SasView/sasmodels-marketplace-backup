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
# // (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
# // (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
# // (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
# // (((((((((((((((((((((((((((((((((+++++++++++++(((((((((((((((((((((((((((((((((
# // (((((((((((((((((((((((((((((++%%%%%%%%%%%%%%%%%++(((((((((((((((((((((((((((((
# // ((((((((((((((((((((((((++%%%%%%%%%%%%%%%%%%%%%%%%%%%++((((((((((((((((((((((((
# // ((((((((((((((((((((++%%%%%%%%%%...............%%%%%%%%%%++((((((((((((((((((((
# // (((((((((((((((((++%%%%%%%%...........%%%...........%%%%%%%%++(((((((((((((((((
# // (((((((((((((((++%%%%%%..............%%%%%..............%%%%%%++(((((((((((((((
# // (((((((((((((++%%%%%%...............%%%%%.................%%%%%%++(((((((((((((
# // ((((((((((((++%%%%%.%%%%%.........%%%%%%....................%%%%%++((((((((((((
# // ((((((((((++%%%%%...%%%%%%%%%%%..%%%%%%.......................%%%%%++((((((((((
# // (((((((((++%%%%%...%%%%%%%%%%%%%%%%%%%.........................%%%%%++(((((((((
# // ((((((((++%%%%%......%%%%%%%%%%%%%%%%%%%%%......................%%%%%++((((((((
# // (((((((++%%%%%.............%%%%%%%%%%%%%%%%%%%%..................%%%%%++(((((((
# // (((((((++%%%%................%%%%%%%%%%%%%%%%%%%%%%%%.............%%%%++(((((((
# // ((((((++%%%%................%%%%%.....%%%%%%%%%%%%%%%%%%%%.........%%%%++((((((
# // ((((((++%%%%..............%%%%%%....%%%%...%%%%%%%%%%%%%%%%%%%%%...%%%%++((((((
# // ((((((++%%%%.............%%%%%%.....%%%%%%%%%....%%%%%%%%%%%%%%%%%%%%%%++((((((
# // (((((++%%%%.............%%%%%......%%%%%%%%%%%%%%%%...%%%%%%%%%%%%..%%%%++(((((
# // (((((++%%%%............%%%%%......%%%%%%%%%%%%%%%%..........%%%%%...%%%%++(((((
# // ((((((++%%%%..........%%%%%......%%%%%%%%%%%%%%%%%.................%%%%++((((((
# // ((((((++%%%%.........%%%%%.......%%%%%%%%%%%%%%%%..................%%%%++((((((
# // ((((((++%%%%..........%%%.......%%%%%%%%%%%%%%%%...................%%%%++((((((
# // (((((((++%%%%..................%%%%%%%%%%%%%%%%...................%%%%++(((((((
# // (((((((++%%%%%.................%%%%%%%%%%%%%%%%..................%%%%%++(((((((
# // ((((((((++%%%%%...............%%%%%%%%%%%%%%%%..................%%%%%++((((((((
# // (((((((((++%%%%%.............%%%%%%%%%%%%%%%%..................%%%%%++(((((((((
# // ((((((((((++%%%%%...........%%%%%%%%%%%%%%%%..................%%%%%++((((((((((
# // ((((((((((((++%%%%%.........%%%%%%%%%%%%%%%%................%%%%%++((((((((((((
# // (((((((((((((++%%%%%%......%%%%%%%%%%%%%%%%...............%%%%%%++(((((((((((((
# // (((((((((((((((++%%%%%%...%%%%%%%%%%%%%%%%..............%%%%%%++(((((((((((((((
# // (((((((((((((((((++%%%%%%%%.....%%%%%%%%%%..........%%%%%%%%++(((((((((((((((((
# // ((((((((((((((((((((++%%%%%%%%%%.....%%%%......%%%%%%%%%%++((((((((((((((((((((
# // ((((((((((((((((((((((((++%%%%%%%%%%%%%%%%%%%%%%%%%%%++((((((((((((((((((((((((
# // (((((((((((((((((((((((((((((++%%%%%%%%%%%%%%%%%++(((((((((((((((((((((((((((((
# // (((((((((((((((((((((((((((((((((+++++++++++++(((((((((((((((((((((((((((((((((
# // (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
# // (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
r"""
Definition
----------

Parameters:
    scale = scaling factor, volume fraction of particles scale phi ~ N V_{sph} / V_{irr}, with N / V_{irr} being the number density of particles in the irradiated volume
    phi_{cyl} = relative volume fraction of cylinders inside the core sphere phi_{cyl} ~ N V_{cyl} / V_{sph,c}, with N / V_{sph,c} being the number density of cylinders in the core sphere
    background = const. background
    R_{sph,c} = core radius of sphere
    d_{sph,sh} = inner shell thickness of sphere
    d_{sph,sh2} = outer shell thickness of sphere
    NB: R_{sph,c} + d_{sph,sh} = radius of whole sphere
    R_{cyl} = radius of one cylinder
    L_{cyl} = length of one cylinder
    R_{avgsph,cyl} = radius of the averaging sphere for the cylinders
    V_{sph} = volume of whole sphere including core and both shells
    V_{sph,i} = volume of sphere including core and inner shell
    V_{sph,c} = volume of sphere core
    V_{cyl} = volume of cylinder
    V_{avgsph,cyl} = volume of the averaging sphere for the cylinders
    sld_{sph,c} = scattering length density of core of sphere
    sld_{sph,sh} = scattering length density of inner shell of sphere
    sld_{sph,sh2} = scattering length density of outer shell of sphere
    sld_{cyl} = scattering length density of cylinders inside the core
    sld_{solv} = scattering length density of solvent


For the particles with a non-spherical symmetry an orientational average is applied:

    F^2(q) = int_{0}^{pi/2} f^2(q,alpha) sin(alpha) dalpha

The output of the 1D scattering intensity function is then given by

    P(q) = frac{	ext{scale}}{V_{sph}} int_0^{pi/2} f^2(q,alpha) sinalpha dalpha + 	ext{background}

where

    f(q,alpha) = ( sld_{sph,sh2} - sld_{solv}    ) * V_{sph}   * f_sph( q*(R_{sph,c} + d_{sph,sh} + d_{sph,sh2}) )
                + ( sld_{sph,sh}  - sld_{sph,sh2} ) * V_{sph,i} * f_sph( q*(R_{sph,c} + d_{sph,sh}) )
                + ( sld_{sph,c}   - sld_{sph,sh}  ) * V_{sph,c} * f_sph( q*R_{sph,c} )
                + ( sld_{cyl}     - sld_{sph,c}   ) * f_sph( q*R_{avgsph,cyl} ) * phi_{cyl} * V_{sph,c} * f_cyl(q,alpha)

    Note: normalization last term
    ( 1/V_{avgsph,cyl} * int exp[imathbf{Q}cdotmathbf{r}_j] d^3mathbf{r}_j ) * N * V_{cyl} * f_cyl = 1/V_{avgsph,cyl} * V_{avgsph,cyl} f_sph(q*R_{avgsph,cyl}) * N * V_{cyl} f_cyl = f_sph(q*R_{avgsph,cyl}) * N * V_{cyl} * f_cyl = V_{sph,c} * phi_{cyl} * f_sph(q*R_{avgsph,cyl}) * f_cyl

    Note: in case of one shell and sld_{cyl} == sld_{sph,sh} and R_{avgsph,cyl} = R_{sph,c} it simplifies to:
    f(q,alpha) = ( sld_{sph,sh} - sld_{solv}   ) * V_{sph} * f_sph( q*(R_{sph,c}+d_{sph,sh}) )
                + ( sld_{sph,c}  - sld_{sph,sh} ) * f_sph( q*R_{sph,c} ) * V_{sph,c} * ( 1.0 - phi_{cyl} f_cyl(q,alpha) )

where

    f_cyl(q,alpha) = j_0( q*L_{cyl}*cos(alpha)/2 ) * 2J1x( q*R_{cyl}sin(alpha) )
    f_sph(x) = 3 * frac{ sin(x)-xcos(x) }{ x^3 }

where

    j_0(x) = sin(x) / x
    2J1x(x) = 2 * J_1(x) / x , where $J_1$ is the first order Bessel function
    V_{cyl} = pi R_{cyl}^2 L_{cyl}
    V_{avgsph,cyl} = 4pi/3 R_{avgsph,cyl}^3
    V_{sph,c} = 4pi/3 R_{sph,c}^3
    V_{sph} = 4pi/3 (R_{sph,c}+d_{sph,sh})^3


For 2D:

The $	heta$ and $phi$ parameters only appear in the model when fitting 2D data. For oriented cylinders, we define the direction of the axis of the cylinder using two angles $	heta$ and $phi$. See cylinder angle definition:

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

name = "coredoubleshellspherefilledwithmanycylinders"
title = "Orientationally averaged form factor for a monodisperse spherical particle with a core-double-shell sphere structure, filled with circular cylinders in its core."
description = """
Note that the platelets inside are monodisperse with a given radius_cylinder and length_cylinder. Their amount is controlled via the fit parameter volume fraction = N * V_cylinder/ V_shpere_core. The randomly distributed positions of the cylinders inside a sphere with radius radius_cylinder_avgsph within the core translates into a form amplitude for a sphere with radius 0 < radius_cylinder_avgsph < radius_sphere_core. Applying polydispersity to the cylinders means to have core-double-shell spheres with cylinders inside, which differ between spheres, but not within one sphere.

Output:
    P(q) = frac{	ext{scale}}{V_{sph}} int_0^{pi/2} f^2(q,alpha) sinalpha dalpha + 	ext{background}

where
    f(q,alpha) = ( sld_{sph,sh2} - sld_{solv}    ) * V_{sph}   * f_sph( q*(R_{sph,c} + d_{sph,sh} + d_{sph,sh2}) )
                + ( sld_{sph,sh}  - sld_{sph,sh2} ) * V_{sph,i} * f_sph( q*(R_{sph,c} + d_{sph,sh}) )
                + ( sld_{sph,c}   - sld_{sph,sh}  ) * V_{sph,c} * f_sph( q*R_{sph,c} )
                + ( sld_{cyl}     - sld_{sph,c}   ) * f_sph( q*R_{avgsph,cyl} ) * phi_{cyl} * V_{sph,c} * f_cyl(q,alpha)

    Note: in case of one shell and sld_{cyl} == sld_{sph,sh} and R_{avgsph,cyl} = R_{sph,c} it simplifies to:
    f(q,alpha) = ( sld_{sph,sh} - sld_{solv}   ) * V_{sph} * f_sph( q*(R_{sph,c}+d_{sph,sh}) )
                + ( sld_{sph,c}  - sld_{sph,sh} ) * f_sph( q*R_{sph,c} ) * V_{sph,c} * ( 1.0 - phi_{cyl} f_cyl(q,alpha) )

where
    f_cyl(q,alpha) = j_0( q*L_{cyl}*cos(alpha)/2 ) * 2J1x( q*R_{cyl}sin(alpha) )
    f_sph(x) = 3 * frac{ sin(x)-xcos(x) }{ x^3 }

where
    j_0(x) = sin(x) / x
    2J1x(x) = 2 * J_1(x) / x , where $J_1$ is the first order Bessel function
    V_{cyl} = pi R_{cyl}^2 L_{cyl}
    V_{avgsph,cyl} = 4pi/3 R_{avgsph,cyl}^3
    V_{sph,c} = 4pi/3 R_{sph,c}^3
    V_{sph} = 4pi/3 (R_{sph,c}+d_{sph,sh})^3

Parameters:
    scale = scaling factor, volume fraction of particles scale phi ~ N V_{sph} / V_{irr}, with N / V_{irr} being the number density of particles in the irradiated volume
    phi_{cyl} = relative volume fraction of cylinders inside the core sphere phi_{cyl} ~ N V_{cyl} / V_{sph,c}, with N / V_{sph,c} being the number density of cylinders in the core sphere
    background = const. background
    R_{sph,c} = core radius of sphere
    d_{sph,sh} = inner shell thickness of sphere
    d_{sph,sh2} = outer shell thickness of sphere
    NB: R_{sph,c} + d_{sph,sh} = radius of whole sphere
    R_{cyl} = radius of one cylinder
    L_{cyl} = length of one cylinder
    R_{avgsph,cyl} = radius of the averaging sphere for the cylinders
    V_{sph} = volume of whole sphere including core and both shells
    V_{sph,i} = volume of sphere including core and inner shell
    V_{sph,c} = volume of sphere core
    V_{cyl} = volume of cylinder
    V_{avgsph,cyl} = volume of the averaging sphere for the cylinders
    sld_{sph,c} = scattering length density of core of sphere
    sld_{sph,sh} = scattering length density of inner shell of sphere
    sld_{sph,sh2} = scattering length density of outer shell of sphere
    sld_{cyl} = scattering length density of cylinders inside the core
    sld_{solv} = scattering length density of solvent
"""
category = "shape:sphere"

#           [ "name", "units", default, [lower, upper], "type", "description"],
#
# convention, first SLDs, then geometry, then orientation
# all functions in C and dict(demo) entries in Py should follow this convention, in order to not mix up params
parameters = [["volfract_cyl", "", 0.4, [0, 1], "", "relative volume fraction of cylinders in core sphere"],
              ["sld_core", "1e-6/Ang^2", 0.0, [-inf, inf], "sld", "core scattering length density"],
              ["sld_shell", "1e-6/Ang^2", 4.0, [-inf, inf], "sld", "inner shell scattering length density"],
              ["sld_shell_2", "1e-6/Ang^2", 4.0, [-inf, inf], "sld", "outer shell scattering length density"],
              ["sld_cyl", "1e-6/Ang^2", 4.0, [-inf, inf], "sld", "cylinder scattering length density"],
              ["sld_solvent", "1e-6/Ang^2", 6.34, [-inf, inf], "sld", "solvent scattering length density"],
              ["sphere_core_radius", "Ang", 500.0, [0, inf], "volume", "sphere core radius"],
              ["sphere_shell_thickness", "Ang", 100.0, [0, inf], "volume", "sphere inner shell thickness"],
              ["sphere_shell_thickness_2", "Ang", 50.0, [0, inf], "volume", "sphere outer shell thickness"],
              ["cyl_radius", "Ang", 400.0, [0, inf], "volume", "cylinder radius"],
              ["cyl_length", "Ang", 250.0, [0, inf], "volume", "cylinder length"],
              ["cyl_avgsph_radius", "Ang", 150.0, [0, inf], "volume", "radius of the averaging sphere for the positioning of the cylinders in the core"],
              ["theta", "degrees", 60, [-360, 360], "orientation", "latitude"],
              ["phi", "degrees", 60, [-360, 360], "orientation", "longitude"]]

source = ["lib/sas_3j1x_x.c", "lib/polevl.c", "lib/sas_J1.c", "lib/gauss76.c", "coredoubleshellspherefilledwithmanycylinders.c"]


# cylinder
# NB: The 2nd virial coefficient of the cylinder is calculated based on the radius and length values, and used as the effective radius for $S(q)$ when $P(q) cdot S(q)$ is applied.
#
#def ER(radius, length):
#  """
#      Return equivalent radius (ER)
#  """
#  ddd = 0.75 * radius * (2 * radius * length + (length + radius) * (length + pi * radius))
#  return 0.5 * (ddd) ** (1. / 3.)


# core-double-shell sphere
# NB: The outer most radius (= radius + thicknesses) is used as the effective radius for $S(Q)$ when $P(Q) cdot S(Q)$ is applied.
# 
def ER(sphere_core_radius, sphere_shell_thickness, sphere_shell_thickness_2):
    """
        Equivalent radius
        @param sphere_core_radius: sphere core radius
        @param sphere_shell_thickness: sphere inner shell thickness
        @param sphere_shell_thickness_2: sphere outer shell thickness
    """
    return sphere_core_radius + sphere_shell_thickness + sphere_shell_thickness_2


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
            volfract_cyl=0.4,
            sld_core=0.0,
            sld_shell=4.0,
            sld_shell_2=2.0,
            sld_cyl=4.0,
            sld_solvent=6.34,
            sphere_core_radius=500,
            sphere_shell_thickness=100,
            sphere_shell_thickness_2=50,
            cyl_radius=400,
            cyl_length=250,
            cyl_avgsph_radius=150,
            theta=60,
            phi=60
)
#            cyl_radius_pd=.2, cyl_radius_pd_n=9,
#            cyl_length_pd=.2, cyl_length_pd_n=10,



qx, qy = 0.2 * np.cos(2.5), 0.2 * np.sin(2.5)
# After redefinition of angles, find new tests values.  Was 10 10 in old coords
tests = [[{}, 0.2, 0.042761386790780453],
        [{}, [0.2], [0.042761386790780453]],
#  new coords
        [{'theta':80.1534480601659, 'phi':10.1510817110481}, (qx, qy), 0.03514647218513852],
        [{'theta':80.1534480601659, 'phi':10.1510817110481}, [(qx, qy)], [0.03514647218513852]],
# old coords   [{'theta':10.0, 'phi':10.0}, (qx, qy), 0.03514647218513852],
#            [{'theta':10.0, 'phi':10.0}, [(qx, qy)], [0.03514647218513852]],
        ]
del qx, qy  # not necessary to delete, but cleaner

