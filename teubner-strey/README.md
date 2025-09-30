# Teubner Strey

Definition This model calculates the scattered intensity of a two-component system using the Teubner-Strey model. Unlike `dab` this function generates a peak. A two-phase material can be characterised by two length scales - a correlation length and a domain size (periodicity). The original paper by Teubner and Strey defined the function as: $$  I(q) \propto \frac{1}{a_2 + c_1 q^2 + c_2 q^4} + \text{background} $$ where the parameters $a_2$, $c_1$ and $c_2$ are defined in terms of the periodicity, $d$, and correlation length $\xi$ as: $$  a_2 = \biggl[1+\bigl(\frac{2\pi\xi}{d}\bigr)^2\biggr]^2\\ c_1 = -2\xi^2\bigl(\frac{2\pi\xi}{d}\bigr)^2+2\xi^2\\ c_2 = \xi^4 $$ and thus, the periodicity, $d$ is given by $$  d = 2\pi\left[\frac12\left(\frac{a_2}{c_2}\right)^{1/2} - \frac14\frac{c_1}{c_2}\right]^{-1/2} $$ and the correlation length, $\xi$, is given by $$  \xi = \left[\frac12\left(\frac{a_2}{c_2}\right)^{1/2} + \frac14\frac{c_1}{c_2}\right]^{-1/2} $$ Here the model is parameterised in terms of  $d$ and $\xi$ and with an explicit volume fraction for one phase, $\phi_a$, and contrast, $\delta\rho^2 = (\rho_a - \rho_b)^2$ : $$  I(q) = \frac{8\pi\phi_a(1-\phi_a)(\Delta\rho)^2c_2/\xi} {a_2 + c_1q^2 + c_2q^4} $$ where `8\pi\phi_a(1-\phi_a)(\Delta\rho)^2c_2/\xi` is the constant of proportionality from the first equation above. In the case of a microemulsion, $a_2 > 0$, $c_1 < 0$, and $c_2 >0$. For 2D data, scattering intensity is calculated in the same way as 1D, where the $q$ vector is defined as $$  q = \sqrt{q_x^2 + q_y^2} $$ References #. M Teubner, R Strey, *J. Chem. Phys.*, 87 (1987) 3195 #. K V Schubert, R Strey, S R Kline and E W Kaler,    *J. Chem. Phys.*, 101 (1994) 5343 #. H Endo, M Mihailescu, M. Monkenbusch, J Allgaier, G Gompper, D Richter,    B Jakobs, T Sottmann, R Strey, and I Grillo,    *J. Chem. Phys.*, 115 (2001), 580 Authorship and Verification **Author:** **Last Modified by:** **Last Reviewed by:**

Definition

This model calculates the scattered intensity of a two-component system using the Teubner-Strey model. Unlike `dab` this function generates a peak. A two-phase material can be characterised by two length scales - a correlation length and a domain size (periodicity).

The original paper by Teubner and Strey defined the function as:

$$  I(q) \propto \frac{1}{a_2 + c_1 q^2 + c_2 q^4} + \text{background} $$ where the parameters $a_2$, $c_1$ and $c_2$ are defined in terms of the periodicity, $d$, and correlation length $\xi$ as:

$$  a_2 = \biggl[1+\bigl(\frac{2\pi\xi}{d}\bigr)^2\biggr]^2\\ c_1 = -2\xi^2\bigl(\frac{2\pi\xi}{d}\bigr)^2+2\xi^2\\ c_2 = \xi^4 $$ and thus, the periodicity, $d$ is given by

$$  d = 2\pi\left[\frac12\left(\frac{a_2}{c_2}\right)^{1/2} - \frac14\frac{c_1}{c_2}\right]^{-1/2} $$ and the correlation length, $\xi$, is given by

$$  \xi = \left[\frac12\left(\frac{a_2}{c_2}\right)^{1/2} + \frac14\frac{c_1}{c_2}\right]^{-1/2} $$ Here the model is parameterised in terms of  $d$ and $\xi$ and with an explicit volume fraction for one phase, $\phi_a$, and contrast, $\delta\rho^2 = (\rho_a - \rho_b)^2$ :

$$  I(q) = \frac{8\pi\phi_a(1-\phi_a)(\Delta\rho)^2c_2/\xi} {a_2 + c_1q^2 + c_2q^4} $$ where `8\pi\phi_a(1-\phi_a)(\Delta\rho)^2c_2/\xi` is the constant of proportionality from the first equation above.

In the case of a microemulsion, $a_2 > 0$, $c_1 < 0$, and $c_2 >0$.

For 2D data, scattering intensity is calculated in the same way as 1D, where the $q$ vector is defined as

$$  q = \sqrt{q_x^2 + q_y^2} $$ References

#. M Teubner, R Strey, *J. Chem. Phys.*, 87 (1987) 3195 #. K V Schubert, R Strey, S R Kline and E W Kaler,    *J. Chem. Phys.*, 101 (1994) 5343 #. H Endo, M Mihailescu, M. Monkenbusch, J Allgaier, G Gompper, D Richter,    B Jakobs, T Sottmann, R Strey, and I Grillo,    *J. Chem. Phys.*, 115 (2001), 580

Authorship and Verification

**Author:** **Last Modified by:** **Last Reviewed by:**

Source: https://marketplace.sasview.org/models/60/
