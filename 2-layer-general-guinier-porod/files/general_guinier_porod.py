import os
import sys
import numpy as np


#name 
name = "general_guinier_porod" 

#title
title = "Generalized Guinier Porod"

#description
description = """
        Guinier-Porod model with TWO Guinier regions.
        rg2 and s2 fit the low-q region
        rg1 and s1 fit the mid-q region
        porod_exp fits the high-q region

        ref: B Hammouda, *A new Guinier-Porod model, J. Appl. Cryst.*, (2010), 43, 716-719."""

#parameters 
parameters = [["rg2", "Ang", 100.0, [0, np.inf], "", "Low-Q Radius of gyration"],
              ["s2",  "",    0.0,  [0, np.inf], "", "Low-Q Dimension variable"],
              ["rg1", "Ang", 10.0, [0, np.inf], "", "Mid-Q Radius of gyration"],
              ["s1",  "",    1.0,  [0, np.inf], "", "Mid-Q Dimension variable"],
              ["porod_exp",  "",    3.0,  [0, np.inf], "", "Porod exponent"]]

# def form_volume(*arg): 
#    return 1.0 

# def ER(*arg): 
#    return 1.0 

def Iq(q, rg2, s2, rg1, s1, porod_exp):

    import numpy as np # somehow this is necessary for the code to function properly

    # preallocate return value
    Iq = 0.0*q

    # Take care of the singular points
    if rg2 <= 0.0 or rg1 <= 0.0 or s2 > s1:
        return Iq

    # Calculate cross-over points and scale factors; the parameter "scale" = G1 multiplies all three pieces
    Q1 = np.sqrt((porod_exp-s1)*(3-s1)/2)/rg1
    Q2 = np.sqrt((s1-s2)/(2*np.power(rg2,2)/(3-s2) - 2*np.power(rg1,2)/(3-s1)))
    D = np.power(rg1,-(porod_exp-s1)) * np.exp(-(porod_exp-s1)/2) * np.power((porod_exp-s1)*(3-s1)/2,(porod_exp-s1)/2)
    G2 = np.exp(-np.power(Q2,2) * (np.power(rg1,2)/(3-s1) - np.power(rg2,2)/(3-s2))) * np.power(Q2,(s2-s1))

    # parse data using Q2 and Q1 transition points
    idx_G2 = q <= Q2
    idx_G1 = np.logical_and((q > Q2),(q <= Q1))
    idx_P = q > Q1

    # Do the calculation and return the function value
    with np.errstate(divide='ignore'):
        Iq[idx_G2] = G2 * np.power(q[idx_G2],-s2) * np.exp(-np.power(q[idx_G2]*rg2,2)/(3-s2))
        Iq[idx_G1] = np.power(q[idx_G1],-s1) * np.exp(-np.power(q[idx_G1]*rg1,2)/(3-s1))
        Iq[idx_P] = D * np.power(q[idx_P],-porod_exp)
    return Iq
Iq.vectorized = True # Iq accepts an array of q values

def Iqxy(x, y, rg2, s2, rg1, s1, porod_exp):
    return Iq(np.sqrt(x*x + y*y), rg2, s2, rg1, s1, porod_exp)
Iqxy.vectorized = True

