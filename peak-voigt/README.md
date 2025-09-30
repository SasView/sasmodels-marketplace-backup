# Peak Voigt

This model describes a pseudo-Voigt shaped peak on a flat background. Definition This pseudo-Voigt peak function is a weighted linear summation of Lorentzian (L) and Gaussian (G) peak shapes. The usefulness of this function is that it produces a peak shape with asymmetry. The scattering intensity $I(q)$ is calculated as $$I(q) = scale . [{W_f.I(q)_L} + {(1-W_f).I(q)_G}] + background$$ where $W_f$ is a weighting factor and $$I(q)_L = \frac{1}{\bigl(1+\bigl(\frac{q-q_0}{HWHM}\bigr)^2\bigr)}$$ $$I(q)_G = \exp\left[ -\frac12 (q-q_0)^2 / \sigma^2 \right]$$ The peak is taken to be centered at $q_0$ with a HWHM (half-width half-maximum) of 1.177 $\sigma$, where $\sigma$ is the standard deviation of the Gaussian. In other words, the widths of the Lorentzian and the Gaussian have been coupled for convenience of parameterisation. When $W_f$ = 1 a Lorentzian peak is returned, and when $W_f$ = 0 a Gaussian peak is returned. For practical purposes 0 < $sigma$ < 0.1 else no peak is generated. For 2D data the scattering intensity is calculated in the same way as 1D, where the $q$ vector is defined as $$q = \sqrt{q_x^2 + q_y^2}$$ References Aaron L. Stancik, Eric B. Brauns A simple asymmetric lineshape for fitting infrared absorption spectra Vibrational Spectroscopy 47 (2008) 66-69 Authorship and Verification Author: Steve King Date: 19/11/2019 Last Modified by: Steve King Date: 24/06/2020 Last Reviewed by: Date:

This model describes a pseudo-Voigt shaped peak on a flat background.

Definition This pseudo-Voigt peak function is a weighted linear summation of Lorentzian (L) and Gaussian (G) peak shapes. The usefulness of this function is that it produces a peak shape with asymmetry. The scattering intensity $I(q)$ is calculated as

$$I(q) = scale . [{W_f.I(q)_L} + {(1-W_f).I(q)_G}] + background$$ where $W_f$ is a weighting factor and

$$I(q)_L = \frac{1}{\bigl(1+\bigl(\frac{q-q_0}{HWHM}\bigr)^2\bigr)}$$

$$I(q)_G = \exp\left[ -\frac12 (q-q_0)^2 / \sigma^2 \right]$$

The peak is taken to be centered at $q_0$ with a HWHM (half-width half-maximum) of 1.177 $\sigma$, where $\sigma$ is the standard deviation of the Gaussian. In other words, the widths of the Lorentzian and the Gaussian have been coupled for convenience of parameterisation.

When $W_f$ = 1 a Lorentzian peak is returned, and when $W_f$ = 0 a Gaussian peak is returned.

For practical purposes 0 < $sigma$ < 0.1 else no peak is generated.

For 2D data the scattering intensity is calculated in the same way as 1D, where the $q$ vector is defined as

$$q = \sqrt{q_x^2 + q_y^2}$$

References Aaron L. Stancik, Eric B. Brauns A simple asymmetric lineshape for fitting infrared absorption spectra Vibrational Spectroscopy 47 (2008) 66-69

Authorship and Verification Author: Steve King Date: 19/11/2019 Last Modified by: Steve King Date: 24/06/2020 Last Reviewed by: Date:

Source: https://marketplace.sasview.org/models/127/
