r"""
Definition
----------
This model comprises three populations of polydisperse hard spheres, 
corresponding to, from the largest to smallest size:
Level0 - The casein micelle, around 100 nm in diameter.
Level1 - Hard regions that resist compression and contain the nanoclusters, 
10-40 nm in diameter.
Level2 - CaP nanoclusters serving as anchors for the casein molecules.

The scattering intensity $I(q)$ is the sum of the intensities scattered 
by the three levels and is calculated as:

$I(q) = c left[ phi _0 v_0 left( Delta p_0 ight) ^2 P_0 left( q ight) + phi _1 v_1 left( Delta p_1 ight) ^2 P_1 left( q ight) + phi _2 v_2 left( Delta p_2 ight) ^2 P_2 left( q ight) ight]$

where $c$ is a constant accounting for the total concentration of the caseins. 
$phi _n$ is the volume fraction occupied by the structural element $n$ in the 
dispersion, while $v_n$ and $Delta p_n$ are its volume and average scattering 
contrast, respectively. $P_n left( q ight)$ are the form factors of each 
object which are modelled using the expression of Aragon et al. (1976). 

The form factors are calculated as:

$P_nleft(qight) = frac{9z!left(z+1ight)^6}{X^6left(z+6ight)!}left[frac{1}{2}+frac{1}{2}left(frac{z+2}{z+1}ight)X^2+left[Gleft(2Xight)^left(1/2ight)left(z+1ight)	imes Q left(Xight)ight]ight]$

where $z = left(frac{1}{sigma}ight)^2 - 1 $ 

with $sigma$ being the polydispersity and

the functions $Gleft(yight)$ and $Qleft(yight)$ are:

$Gleft(yight) = frac{left(z+1ight)^2}{left(z+1ight)^2 + y^2}$ ; $Fleft(yight) = arctanleft[y/left(z + 1ight)ight]$

and

$Qleft(Xight) = - frac{1}{2}cosleft[left(z + 1ight)Fleft(2Xight)ight] - XG^frac{1}{2}left(2Xight)sinleft[left(z + 2ight)Fleft(2Xight)ight] + frac{1}{2}X^2left(frac{z + 2}{z + 1}ight)Gleft(2Xight)cosleft[left(z + 3ight)Fleft(2Xight)ight] $ 


References
----------
Bouchoux, A., Gesan-Guiziou, G., Perez, J. and Cabane, B. (2010). How to
Squeeze a Sponge: Casein Micelles under Osmotic Stress, a SAXS Study.
Biophysical Journal 99, 3754-3762.
Aragon, S. R. and R. Pecora. (1976). Theory of dynamic light scattering 
from polydisperse systems. J. Chem. Phys. 64:2395-2404.
----------------------------
* **Last Modified by:** Jared Raynes **Date:** August 06, 2018
* **Last Reviewed by:** N/A **Date:** July 18, 2018
"""

from numpy import inf, errstate, sin, cos, sqrt, log, exp, pi, square, arctan
from scipy.special import gammaln

name = "bouchoux_casein_micelle"
title = "Three population casein micelle model"
description = """
      Calculates the scattering of a casein micelle
      I(q) = a(P0) + b(P1) + c(P2)
      a = prefactor
      P0 = form factor of micelle
      b = prefactor
      P1 form factor of hard regions
      c = prefactor
      P2 = form factor of CaP nanoclusters
      """
category = "shape:sphere"
# Parameter defaults are from Bouchoux et al Table S5 and use x-ray SLDs
# pylint: disable=bad-whitespace, line-too-long
#   ["name",        "units", default, [min, max], "type",    "description"],
parameters = [
	["radius_0",      "Ang",         417.1, [0, inf],                "volume", "Level0 Sphere radius"],
	["cste",          "",            0.000234414, [0, inf],          "",       "Overall Constant"],
    ["sld_solvent_0", "/Ang^2",      9.40e-6, [-inf, inf],           "sld",    "Level0 Solvent Scattering Length Density"],
    ["sld_0",         "/Ang^2",      9.89e-6, [-inf, inf],           "sld",    "Level0 Scattering Length Density"],
    ["sigma_0",       "",            0.33, [0, 1],                   "",       "Level0 polydispersity"],
    ["na",            "",            1.0, [-inf, inf],               "",       "Relative number density of Level0"],
    ["radius_1",      "Ang",         100.8, [0, inf],                "volume", "Level1 Sphere radius"],
	["sld_1",         "/Ang^2",      10.71e-6, [-inf, inf],          "sld",    "Level1 Layer scattering length density"],
    ["sigma_1",       "",            0.33, [0, 1],                   "",       "Level1 polydispersity"],
    ["nb",            "",            2.713976715351685, [-inf, inf], "",       "Relative number density of Level1"],
    ["radius_2",      "Ang",         15.4, [0, inf],                 "volume", "Level2 Sphere radius"],
	["sld_2",         "/Ang^2",      15.14e-6, [-inf, inf],          "sld",    "Level2 Layer scattering length density"],
    ["sigma_2",       "",            0.20, [0, 1],                   "",       "Level2 polydispersity"],
    ["nc",            "",            168.3, [-inf, inf],             "",       "Relative number density of Level2"]
]

def sphere_form_volume(radius):
	'''
	'''
	return (4.0/3.0)*pi*radius**3.0

def sld_converter(sld):
	'''
	convert sld in A-2 to e-A-1

	>>>sld_converter(9.40e-6)
	0.335
	'''
	e_A = round(sld / 0.0000281, 3)

	return e_A

def prefactor(sld, sld_solvent, radius, cste, n):
	'''
	n = number of casein micelles, assumed constant so set to 1
	'''
	Vma = sphere_form_volume(radius/10.0)
	Dpa = sld_converter(sld) - sld_converter(sld_solvent)
	prefactor = cste * n * (Dpa * Vma)**2
	
	return prefactor	

def aragon(q, radius, sigma):
    '''
    >>> aragon(0.0013, 15.4, 0.20)
    0.9998796784502213
    '''
    dia = radius * 2
    z = (1/((sigma)**2))-1
    b = dia/(z + 1)
    c = z + 1
    d = z + 2
    e = z + 3
    two_X = q * dia
    g_2X = (c**2) / ((c**2)+(two_X**2))
    f_2X = arctan(two_X / c)
    q_X = (-0.5 * cos(c * f_2X))-(((0.5 * two_X) * (g_2X**0.5)) * sin(d * f_2X))+((0.5 * ((0.5 * two_X)**2)) * (d / c) * g_2X * cos(f_2X * e))
    p1 = (9 * exp(gammaln(c)) * (c**6)) / (((0.5*two_X)**6) * exp(gammaln(z + 7)))
    p2 = 0.5 + (0.5 * (d / c) * (( 0.5 * two_X )**2)) + (q_X * (g_2X**(0.5 * c)))
    PX = p1 * p2
    return PX

def Iq(q, 
	radius_0, cste, sld_solvent_0, sld_0, sigma_0, na,
    radius_1, sld_1, sigma_1, nb,
    radius_2, sld_2, sigma_2, nc):
    '''
	>>>Iq(0.0013, 417.1, 0.000234414, 9.40e-6, 9.84e-6, 0.33, 1,
	100.8, 10.87e-6, 0.33, 2.713976715351685, 
	15.4, 1514e-6, 0.20, 168.3)
	5290.302200205034
    Calculate the overall combined scattering
    Calculate prefactors first and then the population scattering
    '''
    Pre_a = prefactor(sld_0, sld_solvent_0, radius_0, cste, na)
    P0 = aragon(q, radius_0, sigma_0)
    Pre_b = prefactor(sld_1, sld_0, radius_1, cste, nb)
    P1 = aragon(q, radius_1, sigma_1)
    Pre_c = prefactor(sld_2, sld_1, radius_2, cste, nc)
    P2 = aragon(q, radius_2, sigma_2)

    inten = (Pre_a * P0) + (Pre_b * P1) + (Pre_c * P2)

    return inten

Iq.vectorized = True  # Iq accepts an array of q values

tests = [
    [{}, 0.0013, 5290.302200205034]
]

demo = dict(scale=1, background=0,
            radius_0=417.3, cste=0.000234414, sld_solvent_0=9.40e-6, sld_0=9.84e-6, sigma_0=0.33, na=1.0,
    		radius_1=100.8, sld_1=10.87e-5, sigma_1=0.33, nb=2.713976715351685,
   			radius_2=15.4, sld_2=15.15e-5, sigma_2=0.20, nc=168.3)