# Two Power Law

Definition The scattering intensity $I(q)$ is calculated as $$  I(q) = \begin{cases} A q^{-m1} + \text{background} & q <= q_c \\ C q^{-m2} + \text{background} & q > q_c \end{cases} $$ where $q_c$ = the location of the crossover from one slope to the other, $A$ = the scaling coefficient that sets the overall intensity of the lower Q power law region, $m1$ = power law exponent at low Q, and $m2$ = power law exponent at high Q.  The scaling of the second power law region (coefficient C) is then automatically scaled to match the first by following formula: $$ C = \frac{A q_c^{m2}}{q_c^{m1}} $$ .. note::     Be sure to enter the power law exponents as positive values! For 2D data the scattering intensity is calculated in the same way as 1D, where the $q$ vector is defined as $$  q = \sqrt{q_x^2 + q_y^2} $$ References None. Authorship and Verification **Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Wojciech Wpotrzebowski **Date:** February 18, 2016 **Last Reviewed by:** Paul Butler **Date:** March 21, 2016

Definition

The scattering intensity $I(q)$ is calculated as

$$  I(q) = \begin{cases} A q^{-m1} + \text{background} & q <= q_c \\ C q^{-m2} + \text{background} & q > q_c \end{cases} $$ where $q_c$ = the location of the crossover from one slope to the other, $A$ = the scaling coefficient that sets the overall intensity of the lower Q power law region, $m1$ = power law exponent at low Q, and $m2$ = power law exponent at high Q.  The scaling of the second power law region (coefficient C) is then automatically scaled to match the first by following formula:

$$ C = \frac{A q_c^{m2}}{q_c^{m1}} $$ .. note::     Be sure to enter the power law exponents as positive values!

For 2D data the scattering intensity is calculated in the same way as 1D, where the $q$ vector is defined as

$$  q = \sqrt{q_x^2 + q_y^2} $$

References

None.

Authorship and Verification

**Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Wojciech Wpotrzebowski **Date:** February 18, 2016 **Last Reviewed by:** Paul Butler **Date:** March 21, 2016

Source: https://marketplace.sasview.org/models/80/
