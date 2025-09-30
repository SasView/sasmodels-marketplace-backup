r"""
Definition
----------
The 1D scattering intensity of two correlated spherical particles can be written as: P(q)=F1^2 + F2^2 + 2*F1*F2*sin(qD)/qD, where F1 and F2 are the scattering amplitudes of particle1 and particle2 respectively, D is the center-to-center distance between the two particles.
Particularly, this model is to calculate the scattering intensity of two spatially correlated hard spheres of different size(radius) and scatterling length density(SLDs) at fixed distance D from each other.

References 
----------
Tianfu Li, Yiyun Cheng, Yu Wang, Hui Wang, Dongfeng Chen, Yuntao Liu, Li Zhang, Wenze Han, Rongdeng Liu , Zijun Wang, Chunming Yang, Charl J. Jafta, Daniel Clemens and and Uwe Keiderling. Analysis of Dimer Impurity in Polyamidoamine Dendrimer Solutions by Small-angle Neutron Scattering[J]. Chinese J. Polym. Sci. doi: 10.1007/s10118-019-2260-x 

Authorship and Verification
---------------------------

* **Author:Tianfu Li, Dongfeng Chen, Paul Butler ** --- **Date:** 2019YYY-03m-28d
* **Last Modified by:** --- **Date:** 2019YYY-03m-28d
* **Last Reviewed by:** --- **Date:** 2019YYY-03m-28d
"""

from math import *
from numpy import inf

name = "correlated_spheres"
title = "User model for correlated_spheres"
description = """two spheres of different size and SL1Ds at fixed distance D from each other """

parameters = [ 
#   ["name", "units", default, [lower, upper], "type", "description"],
    ['Radius1', 'Ang', 20.0, [0, inf], '', 'radius of particle1'],
    ['Radius2', 'Ang', 50.0, [0, inf], '', 'radius of particle2'],
    ['D', 'Ang', 80.0, [0, inf], '', 'center to center distance'],
    ['SLD1', '1e-6/Ang^2', 1.0, [-inf, inf], '', 'scattering length density of particle1'],
    ['SLD2', '1e-6/Ang^2', 2.0, [-inf, inf], '', 'scattering length density of particle2'],
    ['SLDsolvent', '1e-6/Ang^2', 6.38, [-inf, inf], '', 'scattering length density of solvent'],
    ]
def Iq(x, Radius1, Radius2, D, SLD1, SLD2, SLDsolvent):
    """Absolute scattering"""
    qr1 = x * Radius1
    qr2 = x * Radius2
    qD = x * D
    sn1 = sin(qr1)
    cn1 = cos(qr1)
    sn2 = sin(qr2)
    cn2 = cos(qr2)  
    bes1 = 3 * (sn1 * qr1 * cn1) / qr1**3
    bes1[qr1 == 0] = 1
    bes2 = 3 * (sn2 * qr2 * cn2) / qr2**3
    bes2[qr2 == 0] = 1
    fq1 = bes1 * (SLD1 - SLDsolvent) * 1.33333333333 * pi * Radius1**3
    fq2 = bes2 * (SLD2 - SLDsolvent) * 1.33333333333 * pi * Radius2**3
    Intensity = 1.0e-4 * (fq1**2 + fq2**2 + fq1 * fq2 *sin(qD)/qD)
    
    return Intensity
## uncomment the following if Iq works for vector x
#Iq.vectorized = True

#def Iqxy(x, y, Radius1, Radius2, D, SLD1, SLD2, SLDsolvent):
#    """Absolute scattering of oriented particles."""
#    ...
#    return oriented_form(x, y, args)
## uncomment the following if Iqxy works for vector x, y
#Iqxy.vectorized = True
