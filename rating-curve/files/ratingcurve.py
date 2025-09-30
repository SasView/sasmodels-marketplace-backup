r"""

Hydrological rating curve.

Definition
----------

THIS MODEL IS NOT INTENDED FOR THE ANALYSIS OF SAXS/SANS DATA!

This model is in part provided to illustrate the utility of SasView as a fitting
program for the analysis of input data that is *not* $I(q)$ vs $q$. But at the
same time it usefully provides a means of fitting or calculating hydrological
stage-discharge data.

The relationship between the stage, $h$, the water level at a monitoring station,
and corresponding discharge, or flow, $Q$, is expressed by a Rating Curve of the
form:

.. math::

    Q(h) = K \cdot \left( h - \alpha \right)^{\beta}
    
 where $K$ and \beta are constants and \alpha is the stage at zero flow.

Input Data
----------

The input data can be in any data format recognised by the SasView data loader,
though a format containing delimited two-column ASCII text will probably be the
most convenient.

SasView will look for the first pair of numerical values in the file, so it is
permissible to prefix the data with some lines of metadata and/or column
headers, but none of these will be imported. If the file contains multiple data
blocks it is likely that only the first one will be imported, so it is important
that the data you want to fit is the first data block in the file.

Whatever the file format it is imperative that the correct data is placed in
these the two columns::

    Column 1: what would normally be $q$:    Stage (water level), $h$
    
    Column 2: what would normally be $I(q)$: Discharge, $Q(h)$

Using this Model
----------------

SasView appends *scale* and *background* parameters to all of its models but
these parameters have no meaning in this model. Set them to 1.0 and 0.0,
respectively.

References
----------

#.  https://en.wikipedia.org/wiki/Rating_curve. 
#.  https://nrfa.ceh.ac.uk/ratings-datums.

Verification
------------

The model has not been verified.

Authorship History
------------------

* **Author:** Steve King **Date:** 26/08/2020
* **Last Modified by:** **Date:**
* **Last Reviewed by:** **Date:**

"""
import numpy as np
from numpy import inf

name = "ratingcurve"
title = "Rating Curve"
description = """
    Computes a stage-discharge
    curve. READ THE DOCS!
"""
category = "shape-independent"
structure_factor = False
single = False

#   ["name", "units", default, [lower, upper], "type","description"],
parameters = [
    ["K", "", 1.0, [-inf, inf], "", "constant"],
    ["alpha", "(height)", 0.0, [-inf, inf], "", "datum corr."],
    ["beta", "", 2.5, [0, inf], "", "exponent"],
]

def Iq(q, K, alpha, beta):

    result = K * np.power((q - alpha),beta)
    
    return result
	
Iq.vectorized = True  # Iq accepts an array of q values
