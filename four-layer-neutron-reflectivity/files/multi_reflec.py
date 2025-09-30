# Four slab model
# cylinder model
# Note: model title and parameter table are inserted automatically
r"""
    
    For information about polarised and magnetic scattering, see
    the :ref:`magnetism` documentation.
    
    Definition
    ----------
    
    Calculates specular reflectivity for upto 4 slab-like layers on a substrate. Follows Parratt formulism[1]:
    
    .. math:
    R_n=frac{r_{n,n+1}+R_{N+1}exp{2id_{n+1}k_{z,n+1}}{1+r_{n.n+1}R_{n+1}exp{2id_{n+1}k_{z,n+1}}
    
    Each layer is characterised by: scattering lenght density [A^-2], Thickness [A], and Roughness[A].
    
    SLD of capping medium can be set. As can SLD and roughness of substrate.
    
    Effect of roughness follows Nevot and Croce[2]. e.g.
    .. math::
        r_{ij}=frac{k_i-k_j}{k_i+k_j}exp -0.5k_ik_jsigma^2
        
        where $r_{ij}$ is the fresnel reflection term between layers $i$ and $j$, and $sigma$ is the roughness of this interface.

    Validation
    ----------
    
    Validation of the code was done by comparing the output of the model to the output of the online neutron reflectivity calculator produced by NIST (https://www.ncnr.nist.gov/instruments/magik/calculators/reflectivity-calculator.html). The NIST software uses an alternative method to generate the relfectivity (Abeles). This model appears to match the NIST one well.
    
    .. figure:: NR_comparison.png
   
    
    References
    ----------
    
    [1] "Surface Studies of Solids by Total Refiection of X-Rays", L. G. Parratt, Physical Review, V95(2), 1954, pp 359-369.
    [2] L. Nevot and P. Croce, Appl. Phys. 15, 761 1980.
    
    Authorship and Verification
    ----------------------------
    
    * **Author:** Simon Martin **Date:** December 15, 2017
    * **Last Modified by:** Simon Martin **Date:** December 15, 2017
    * **Last Reviewed by:** N/A **Date:** N/A
    """


from math import *
import os
import sys
import numpy

opencl=False

#name
name = "NR_4_slab"

#title
title = "User 4 layer model for neutron_reflecticity"

#description
description = "Calculates reflectivity for up to 4 layers (characterised by SLD, thickness, and roughness) on substrate of SLD sld_s, roughness r_s."

#parameters

#parameters = [
#              ['sld_cap', '1e-6/Ang^2', 0., [0., numpy.inf], 'sld', 'Capping SLD'],
#              ['sld1', '1e-6/Ang^2', 0., [0., numpy.inf], 'sld', 'Layer SLD'],
#             ['t1', '1/Ang', 0., [0., numpy.inf], 'length', 'Layer thickness'],
#              ['r1', '1/Ang', 0., [0., numpy.inf], 'length', 'Layer roughness'],
#              ['sld2', '1e-6/Ang^2', 0., [0., numpy.inf], 'sld', 'Layer SLD'],
#              ['t2', '1/Ang', 0., [0., numpy.inf], 'length', 'Layer thickness'],
#              ['r2', '1/Ang', 0., [0., numpy.inf], 'length', 'Layer roughness'],
#              ['sld3', '1e-6/Ang^2', 0., [0., numpy.inf], 'sld', 'Layer SLD'],
#              ['t3', '1/Ang', 0., [0., numpy.inf], 'length', 'Layer thickness'],
#              ['r3', '1/Ang', 0., [0., numpy.inf], 'length', 'Layer roughness'],
#              ['sld4', '1e-6/Ang^2', 0., [0., numpy.inf], 'sld', 'Layer SLD'],
#              ['t4', '1/Ang', 0., [0., numpy.inf], 'length', 'Layer thickness'],
#              ['r4', '1/Ang', 0., [0., numpy.inf], 'length', 'Layer roughness'],
#              ['sld_s', '1e-6/Ang^2', 2.07, [0., numpy.inf], 'sld', 'Substrate SLD'],
#              ['r_s', '1/Ang', 10, [0., numpy.inf], 'length', 'substrate roughness'],
#              ]

parameters = [
              ['sld_cap', '', 0., [0., numpy.inf], '',''],
              ['sld1', '', 0., [0., numpy.inf], '',''],
              ['t1', '', 0., [0., numpy.inf], '',''],
              ['r1', '', 0., [0., numpy.inf], '',''],
              ['sld2', '', 0., [0., numpy.inf], '',''],
              ['t2', '', 0., [0., numpy.inf], '',''],
              ['r2', '', 0., [0., numpy.inf], '',''],
              ['sld3', '', 0., [0., numpy.inf], '',''],
              ['t3', '', 0., [0., numpy.inf], '',''],
              ['r3', '', 0., [0., numpy.inf], '',''],
              ['sld4', '', 2., [0., numpy.inf], '',''],
              ['t4', '', 100., [0., numpy.inf], '',''],
              ['r4', '', 10., [0., numpy.inf], '',''],
              ['sld_s', '', 2.07, [0., numpy.inf], '',''],
              ['r_s', '', 10, [0., numpy.inf], '',''],
              ]
source = ["lib/sas_3j1x_x.c", "multi_reflec.c"]
