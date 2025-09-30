# Broad Peak

Definition This model calculates an empirical functional form for SAS data characterized by a broad scattering peak. Many SAS spectra are characterized by a broad peak even though they are from amorphous soft materials. For example, soft systems that show a SAS peak include copolymers, polyelectrolytes, multiphase systems, layered structures, etc. The d-spacing corresponding to the broad peak is a characteristic distance between the scattering inhomogeneities (such as in lamellar, cylindrical, or spherical morphologies, or for bicontinuous structures). The scattering intensity $I(q)$ is calculated as $$ I(q) = \frac{A}{q^n} + \frac{C}{1 + (|q - q_0|\xi)^m}^p + B $$ Here the peak position is related to the d-spacing as $q_0 = 2\pi / d_0$. $A$ is the Porod law scale factor, $n$ the Porod exponent, $C$ is the Lorentzian scale factor, $m$ the exponent of $q$, $\xi$ the screening length, and $B$ the flat background. $p$ generalizes the model. With m = 2 and p = 1 the Lorentz model is obtained whereas for m = 2 and p = 2 the Broad-Peak model is identical to the Debye-Anderson-Brumberger (dab) model. For 2D data the scattering intensity is calculated in the same way as 1D, where the $q$ vector is defined as $$ q = \sqrt{q_x^2 + q_y^2} $$ References None. Authorship and Verification **Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Dirk Honecker **Date:** May 28, 2021 **Last Reviewed by:** Richard Heenan **Date:** March 21, 2016

Definition

This model calculates an empirical functional form for SAS data characterized by a broad scattering peak. Many SAS spectra are characterized by a broad peak even though they are from amorphous soft materials. For example, soft systems that show a SAS peak include copolymers, polyelectrolytes, multiphase systems, layered structures, etc.

The d-spacing corresponding to the broad peak is a characteristic distance between the scattering inhomogeneities (such as in lamellar, cylindrical, or spherical morphologies, or for bicontinuous structures).

The scattering intensity $I(q)$ is calculated as

$$ I(q) = \frac{A}{q^n} + \frac{C}{1 + (|q - q_0|\xi)^m}^p + B $$ Here the peak position is related to the d-spacing as $q_0 = 2\pi / d_0$.

$A$ is the Porod law scale factor, $n$ the Porod exponent, $C$ is the Lorentzian scale factor, $m$ the exponent of $q$, $\xi$ the screening length, and $B$ the flat background. $p$ generalizes the model. With m = 2 and p = 1 the Lorentz model is obtained whereas for m = 2 and p = 2 the Broad-Peak model is identical to the Debye-Anderson-Brumberger (dab) model.

For 2D data the scattering intensity is calculated in the same way as 1D, where the $q$ vector is defined as

$$ q = \sqrt{q_x^2 + q_y^2} $$ References

None.

Authorship and Verification

**Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Dirk Honecker **Date:** May 28, 2021 **Last Reviewed by:** Richard Heenan **Date:** March 21, 2016

Source: https://marketplace.sasview.org/models/30/
