"""

DLS analysis by the method of Cumulants.

Definition
----------

THIS MODEL IS NOT INTENDED FOR THE ANALYSIS OF SAXS/SANS DATA!

This model is in part provided to illustrate the utility of SasView as a fitting
program for the analysis of input data that is *not* $I(q)$ vs $q$. But at the
same time it usefully provides a basic means of analysing Dynamic Light
Scattering (DLS) data using the Method of Cumulants (Koppel, 1972).

.. Note:: The Method of Cumulants is only valid if the particle size
          distribution is monomodal. However, the size distribution can be
          polydisperse.
      
Input Data
----------

The input data can be in any data format recognised by the SasView data loader,
though a format containing delimited two-column ASCII text will probably be the
most convenient.

SasView will look for the first pair of numerical values in the file, so it is
permissible to prefix the data with some lines of metadata and/or column
headers, but none of these will be imported. If the file contains multiple data
blocks it is likely that only the first one will be imported, so it is important
that the data you want to fit is the first data block in the file. This
reasonable degree of flexibility means that in some instances data files output
by commercial correlators can be read by SasView 'as is', without any need for
reformatting.

For example, this is a text format output by an LSi Correlator (see
https://lsinstruments.ch/en/) ::
    
    03/08/2020	17:30 PM
    Pseudo Cross Correlation
    Scattering angle:	110.0
    Duration (s):	60
    Wavelength (nm):	642.0
    Refractive index:	1.330
    Viscosity (mPas):	0.854
    Temperature (K):	309.0
    Laser intensity (mW):	0.0
    Average Count rate  A (kHz):	19388.1
    Average Count rate  B (kHz):	19388.1
    Intercept:	1.0000
    Cumulant 1st	-Inf
    Cumulant 2nd	-Inf	NaN
    Cumulant 3rd	-Inf	NaN

    Lag time (s)         g2-1
    0.000000e+00	2.153341e+02
    1.250000e-08	-1.000000e+00
    2.500000e-08	1.897621e-02
    3.750000e-08	1.454616e+00
    5.000000e-08	1.040391e+00
    6.250000e-08	9.113997e-01
    7.500000e-08	8.547216e-01
    8.750000e-08	8.269044e-01
    1.000000e-07	7.905431e-01
    1.125000e-07	7.863978e-01
    1.250000e-07	7.645010e-01
    1.375000e-07	7.728501e-01
    1.500000e-07	7.646473e-01
    1.625000e-07	7.516946e-01
    1.750000e-07	7.575662e-01
    1.875000e-07	7.556643e-01
    2.000000e-07	7.547962e-01
    ...
    5.033165e+01	-5.472073e-03

    Count Rate History (KHz)  CR CHA / CR CHB
    0.000000	18560.000000	18560.000000
    ...
    59.926118	16078.000000	16078.000000

In this example, SasView ignores all the metadata preceding the first (two-
column) data block, the correlation function, and ignores everything after the
two-column data block.

Whatever the file format it is imperative that the correct data is placed in
these the two columns::

    Column 1: what would normally be $q$:    Correlator time or $Tau$
                                             (in seconds)
    
    Column 2: what would normally be $I(q)$: Normalised Intensity Autocorrelation
                                             Function, $G2(Tau)$

Method of Analysis
------------------

For a monomodal dispersion of **monodisperse** scatterers

.. math::

    G2(	au) = 	ext{A} cdot exp(-2 Gamma 	au) + 	ext{background}

where $Gamma = D cdot q^2$ is the decay rate, $D$ is the mutual diffusion
coefficient and $q$ is the scattering vector.

For a monomodal dispersion of **polydisperse** scatterers Koppel showed

(FORMULA 1)

.. math::

    G2(	au) = 	ext{A} cdot exp(-2 Gamma_1 	au + Gamma_2 	au^2 -
    (1/3) Gamma_3 	au^3 + ...) + 	ext{background}

where each $Gamma$ is a cumulant of the distribution of decay rates arising
from the different sized scatterers. However, this function is unstable. A more
stable function is (Pusey et al, 1974; Frisken, 2001; Mailer et al, 2015)

(FORMULA 2)

.. math::

    G2(	au) = 	ext{A} cdot exp(-2 Gamma_1 	au) cdot
    (1 + (1/2) Gamma_2 	au^2) - (1/6) Gamma_3 	au^3 + ...)^2
    + 	ext{background}

Here $Gamma_1$ is now the *average* decay rate (representing a weighted average
of the different diffusion coefficients) and $Gamma_2$ is related to the
relative polydispersity index, $PDI = Gamma_2 / Gamma_1^2$.

.. Note:: This PDI must not be confused with dispersity indicies measured by
          static light-scattering (where it is the ratio of the weight-average
          molar mass to the number-average molar mass, Mw/Mn), viscometry, etc.
          The PDI from DLS has a range of 0-1 where, in theory, a value of 0
          represents a monodisperse system. In the case of Mw/Mn dispersity, a
          monodisperse system is represented by a value of 1!
          
In practical terms, a PDI of <0.05 is indicative of a monodisperse system. PDI's
of 0.1 to 0.7 represent systems that are nearly monodisperse, whereas a PDI >0.7
suggests significant polydispersity (Stetefeld et al, 2016). For more
information, also see the section Polydispersity & Orientational Distributions
in the SasView User Documentation.

The third cumulant is related to the *skewness* of the decay rate distribution
($Gamma_3 / Gamma_2^{3/2}$) and the fourth cumulant (not implemented in this
model) gives the *kurtosis* ($Gamma_4 / Gamma_2^2$). Further cumulants are
rarely, if ever, used.

FORMULA 2 is used by default in this model, but both formulae are provided
below. Simply comment/uncomment whichever is required.

Mutual Diffusion Coefficient & Size
-----------------------------------

The usefulness of $D$ is that it is related to the size and shape of the
scatterers through

.. math::

    D = frac{k_B T}{f}
    
where $k_B$ is the Boltzmann Constant, $T$ is the absolute temperature, and $f$
is a quantity called the Friction Factor. This relationship is valid so long as
the system is dilute.

In the case of spherical scatterers Stoke's Law gives $f = 6 pi eta R$
where $eta$ is the viscosity of the dispersion medium and $R$ is the radius of
the spheres. Combining these two functions then leads to the well-known Stokes-
Einstein relation

.. math::

    D = frac{k_B T}{6 pi eta R}
    
It is this function that this model uses to compute a radius. If the system is
polydisperse then $R$ is a z-average value.

If the scatterers are not spherical then either $f$ or $R$ must be adjusted
accordingly.

Using this Model
----------------

The parameters *angle*, *temperature*, *viscosity*, *ref_index*, and *wavelength*
are for defining the experimental conditions to enable the correct calculation
of $R$. **They must not be fitted!** Do not tick their checkboxes.

The *scale* parameter will be what many commercial DLS software packages refer
to as the *Intercept* of the correlation function. This must be between 0 and 1,
but for the data to have any real meaning it should be between 0.6 and 1.

If the correlator has supplied its output as $G2(	au)-1$ (as in the data file
example above) then *background* should be esentially zero.

Do not attempt to fit all of the tail of the correlation function. Use the min
and max $q$-range for fitting boxes to limit the fit range to a sensible region
of the correlation function. You only need to fit the decay and the start of the
tail.

The best way to approach fitting the data is to gradually increase the number of
cumulants being fitted. So, initially, set *pdi* and *cumulant3* to zero, and fit
(check the boxes) the parameters *scale*, *background* and *radius*. Then fit
the *pdi*. Then (if required) fit *cumulant3*.

To view the fit it will probably be helpful to change the y-axis scale from the
SasView default of log(y) to y. To do this, right-click on the graph. It is
also possible to change the x and y axis labels from their SasView defaults of
$q$ and $intensity$.

Notes
-----

This model is inspired by a similar model in the SASfit model-fitting package
(Kohlbrecher, 2020).

References
----------

#.  D. E. Koppel. Analysis of macromolecular polydispersity in intensity
    correlation spectroscopy: The method of cumulants. The Journal of Chemical
    Physics, (1972), 57(11), 4814-4820. 
#.  P. N. Pusey, D. E. Koppel, D. E. Schaefer, R. D. Camerini-Otero, and S. H.
    Koenig. Intensity fluctuation spectroscopy of laser light scattered by
    solutions of spherical viruses. r17, q.beta., BSV, PM2, and t7. i. light-
    scattering technique. Biochemistry, (1974), 13(5), 952-960.
#.  B. J. Frisken. Revisiting the method of cumulants for the analysis of
    dynamic light-scattering data. Applied Optics, (2001), 40(24), 4087.
#.  A. G. Mailer, P. S. Clegg, and P. N. Pusey. Particle sizing by dynamic
    light scattering: nonlinear cumulant analysis. Journal of Physics: Condensed
    Matter, (2015), 27(14), 145102.
#.  J. Stetefeld, S. A. McKenna1 & T. R. Patel. Dynamic light scattering: a
    practical guide and applications in biomedical sciences. Biophys Rev (2016),
    8, 409-427.
#.  J. Kohlbrecher. User guide for the SASfit software package. Chapter 13.
    June 2020.

Verification
------------

The model has been tested by comparing its output to that from the commercial
LSi correlator software using the same input data and range of $	au$.

For a nominal 30 nm diameter PS latex standard::

    LSi    : intercept = 0.750, radius = 13.7  nm, width = 2.89 nm
    SasView: intercept = 0.743, radius = 13.64 nm, pdi   = 0.089
    
For a PNIPAM microgel::

    LSi    : intercept = 0.694, radius = 275   nm, width = 90.6 nm
    SasView: intercept = 0.716, radius = 290.0 nm, pdi   = 0.675
    
Both sets of fits reproduce the $intercept$ well, and recognise a big difference
between the polydispersity of the samples, although it appears that as the
polydispersity increases the reliability of the $radius$ parameter is called
into question. However, visually, SasView appears to do a much better job of
fitting the data than the commercial software. This may reflect the fact that
SasView has much better optimisers.

Authorship History
------------------

* **Author:** Steve King **Date:** 25/08/2020
* **Last Modified by:** **Date:**
* **Last Reviewed by:** **Date:**

"""
import numpy as np
from numpy import inf

name = "cumulants_dls"
title = "DLS analysis by Cumulants"
description = """
    Computes radius & poly-
    dispersity index from DLS
    data using the method of
    Cumulants. READ THE DOCS!
"""
category = "shape-independent"
structure_factor = False
single = False

#   ["name", "units", default, [lower, upper], "type","description"],
parameters = [
    ["angle", "degrees", 110.0, [0.0, 360.0], "", "scattering angle"],
    ["temperature", "degC", 25.0, [-273.16, inf], "", "sample temperature"],
    ["viscosity", "mPas/cP", 0.894, [0.0, inf], "", "solvent viscosity"],
    ["ref_index", "", 1.33, [1.00, 2.42], "", "solvent refractive index"],
    ["wavelength", "nm", 642.0, [400.0, 800.0], "", "laser wavelength"],
    ["radius", "nm", 100.0, [0.01, inf], "", "z-ave spherical radius"],
    ["pdi", "", 0.1, [0.0, inf], "", "dls polydispersity index"],
    ["cumulant3", "", 0.0, [-inf, inf], "", "3rd cumulant"],
]

def Iq(q, angle, temperature, viscosity, ref_index, wavelength, radius, pdi, cumulant3):
    pi = 3.141592654
    kB = 1.38064852e-23
    Tabs = 273.16+temperature
    viscosity_in_si = viscosity/1000.0
    wavelength_in_m = wavelength/1.0e+09
    radius_in_m = radius/1.0e+09
    QQ = np.power((4.0*pi*ref_index/wavelength_in_m)*np.sin(angle/2.0),2.0)
    
    cumulant1 = (kB*Tabs*QQ)/(6.0*pi*viscosity_in_si*radius_in_m)
    cumulant2 = pdi*np.power(cumulant1,2.0)

#    FORMULA 1    
#    result = 
#    np.exp((-2.0*cumulant1*q)+(cumulant2*np.power(q,2.0))- 
#    ((1.0/3.0)*cumulant3*np.power(q,3.0)))

#   FORMULA 2
    result = 
    np.exp(-2.0*cumulant1*q)*np.power((1.0+(cumulant2*np.power(q,2.0)/2.0)- 
    (cumulant3*np.power(q,3.0)/6.0)),2.0)
    
    return result
	
Iq.vectorized = True  # Iq accepts an array of q values

tests = [
    [{'scale': 0.9, 'background' : 0.001, 'angle' : 110.0,
      'temperature' : 25.0, 'viscosity' : 0.894, 'ref_index' : 1.33,
      'wavelength' : 642.0, 'radius' : 100.0, 'pdi' : 0.1,
      'cumulant3' : 0.0},
     [1.0e-06, 0.01], [0.898026606959, 0.0010000000008228433]],
	]
