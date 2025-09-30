# Sphere Concentration A

Spheres with uniform scattering length density reparameterized to used to use the *volume number density* of spheres, NOT the volume fraction of spheres as in the normal SasView sphere model. Also note that, unlike most other SasView models, the scattering length densities (SLDs) and spherical radius in this model must be input in cm^-2 and nm, respectively. Definition The 1D scattering intensity is calculated in the following way (Guinier, 1955) $$  I(q) = \text{scale} \cdot \text{N} \cdot \left[ 3V(\Delta\rho) \cdot \frac{\sin(qr) - qr\cos(qr))}{(qr)^3} \right]^2 + \text{background} $$ where $N$ is the *volume number density* of spheres, $V$ is the volume of one sphere, $r$ is the radius of a sphere and $background$ is the background level. $sld$ and $sld_solvent$ are the scattering length densities (SLDs) of the spheres and the solvent (or matrix) respectively, whose difference is $\Delta\rho$. Note that if your data is on an absolute scale, then $scale$ in this model should be unity! Otherwise $scale$ is just an arbitrary scaling factor. Also remember that packing constraints mean $$ N \neq \frac{1}{V} $$ The 2D scattering intensity is the same as above, regardless of the orientation of $\vec q$. Validation This model was validated against the sphere model. References 1. A Guinier and G. Fournet, *Small-Angle Scattering of X-Rays*, John Wiley and Sons, New York, (1955) Authorship and Verification Author: Olivier Tache Date: 20/05/2020 Last Modified by: Steve King Date: 21/05/2020 Last Reviewed by: Date:

Spheres with uniform scattering length density reparameterized to used to use the *volume number density* of spheres, NOT the volume fraction of spheres as in the normal SasView sphere model.

Also note that, unlike most other SasView models, the scattering length densities (SLDs) and spherical radius in this model must be input in cm^-2 and nm, respectively.

Definition

The 1D scattering intensity is calculated in the following way (Guinier, 1955)

$$  I(q) = \text{scale} \cdot \text{N} \cdot \left[ 3V(\Delta\rho) \cdot \frac{\sin(qr) - qr\cos(qr))}{(qr)^3} \right]^2 + \text{background} $$

where $N$ is the *volume number density* of spheres, $V$ is the volume of one sphere, $r$ is the radius of a sphere and $background$ is the background level. $sld$ and $sld_solvent$ are the scattering length densities (SLDs) of the spheres and the solvent (or matrix) respectively, whose difference is $\Delta\rho$.

Note that if your data is on an absolute scale, then $scale$ in this model should be unity! Otherwise $scale$ is just an arbitrary scaling factor.

Also remember that packing constraints mean

$$ N \neq \frac{1}{V} $$

The 2D scattering intensity is the same as above, regardless of the orientation of $\vec q$.

Validation

This model was validated against the sphere model.

References

1. A Guinier and G. Fournet, *Small-Angle Scattering of X-Rays*, John Wiley and Sons, New York, (1955)

Authorship and Verification

Author: Olivier Tache Date: 20/05/2020 Last Modified by: Steve King Date: 21/05/2020 Last Reviewed by: Date:

Source: https://marketplace.sasview.org/models/125/
