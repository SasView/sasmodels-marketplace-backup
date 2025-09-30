r"""

Spheres with uniform scattering length density reparameterized to used
to use the *volume number density* of spheres, NOT the volume fraction
of spheres as in the normal SasView sphere model.

Also note that, unlike most other SasView models, the scattering length
densities (SLDs) and spherical radius in this model must be input in
cm^-2 and nm, respectively.

Definition
----------

The 1D scattering intensity is calculated in the following way (Guinier, 1955)

.. math::

    I(q) = 	ext{scale} cdot 	ext{N} cdot left[
        3V(Deltaho) cdot frac{sin(qr) - qrcos(qr))}{(qr)^3}
        ight]^2 + 	ext{background}

where $N$ is the *volume number density* of spheres, $V$ is the volume
of one sphere, $r$ is the radius of a sphere and *background* is the
background level. *sld* and *sld_solvent* are the scattering length
densities (SLDs) of the spheres and the solvent (or matrix) respectively,
whose difference is $Deltaho$.

Note that if your data is on an absolute scale, then *scale* in this model
should be unity! Otherwise *scale* is just an arbitrary scaling factor.

Also remember that packing constraints mean $N 
eq frac{1}(V}$.

The 2D scattering intensity is the same as above, regardless of the
orientation of $vec q$.

Validation
----------

This model was validated against the sphere model.


References
----------

#. A Guinier and G. Fournet, *Small-Angle Scattering of X-Rays*,
   John Wiley and Sons, New York, (1955)

Authorship and Verification
----------------------------

* **Author:** Olivier Tache **Date:** 20/05/2020
* **Last Modified by:** Steve King **Date:** 21/05/2020
* **Last Reviewed by:** **Date:**
"""

from sasmodels.special import *
from numpy import pi, inf, sin, cos, sqrt, log

name = "sphere_concentration"
title = "Spheres with uniform SLD but using number density"
description = """
P(q)=scale*N*[3V*(sld-sld_solvent)*(sin(qr)-qr cos(qr))
              /(qr)^3]^2 + background
    r: radius of sphere
    V: volume of the sphere
    N: volume number density
    sld: SLD of the sphere
    sld_solvent: SLD of the matrix
"""

parameters = [ 
#   ["name", "units", default, [lower, upper], "type", "description"],
    ['sld', '1/cm^2', 1.0e10, [-inf, inf], '', 'Sphere scattering length density'],
    ['sld_solvent', '1/cm^2', 6.0e10, [-inf, inf], '', 'Solvent scattering length density'],
    ['concentration', '1/cm^3', 6.4e19, [0, inf], '', 'Volume number density of spheres'],
    ['diameter', 'nm', 10, [0, inf], 'volume', 'Sphere radius'],
    ]
    
def Iq(x, sld, sld_solvent, concentration, diameter):
    """Absolute scattering"""
    def P1(q,R):
        """
        This function returns the form factor of a sphere of radius R for q
        """
        
        return F1(q,R)**2.
    
    def F1(q,R):
        """
        This function returns a scattering amplitude of a sphere of radius R for q
        """
        return (3.0*(sin(q*R)-q*R*cos(q*R)))/(q*R)**3.0
    
    def sphere(q,par):
        '''
        par[0] diameter of the sphere (nm)
        par[1] scattering length density of sphere (cm-2)
        par[2] scattering length density of outside (cm-2)
        par[3] concentration of sphere (cm-3)
        '''
        diameter=par[0]
        radiusA=(diameter/2.)*10.   #convert to radius in Angstroms
        I=par[3]*(par[1]-par[2])**2.*form_volume(radiusA)**2.*1.e-48*P1(q,radiusA)
        return I
    
    return sphere(x,[diameter,sld,sld_solvent,concentration])
    
## uncomment the following if Iq works for vector x
Iq.vectorized = True

def form_volume(diameter):
    """
    Volume of the particles used to compute absolute scattering intensity
    and to weight polydisperse parameter contributions.
    """
    radius=(diameter/2.)*10.   #convert to radius in Angstroms
    return 1.333333333333333 * pi * radius ** 3.

def ER(diameter):
    """
    Effective radius of particles to be used when computing structure factors.

    Input parameters are vectors ranging over the mesh of polydispersity values.
    """
    return (diameter/2.)*10.

#def VR(diameter):
#    """
#    Volume ratio of particles to be used when computing structure factors.
#
#    Input parameters are vectors ranging over the mesh of polydispersity values.
#    """
#    return 1.0

#def Iqxy(x, y, sld, sld_solvent, concentration, diameter):
#    """Absolute scattering of oriented particles."""
#    ...
#    return oriented_form(x, y, args)
## uncomment the following if Iqxy works for vector x, y
#Iqxy.vectorized = True

tests = [
   [{'scale': 1.0, 'background' : 0.3, 'sld': 3.16e10, 'sld_solvent': 6.35e10,
     'concentration': 6.4e17, 'diameter': 15.0},
     [0.00200453398091 , 0.237595891284], [18.2015211186, 0.300508833488]],
	]
