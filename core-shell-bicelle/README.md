# Core Shell Bicelle

Definition This model provides the form factor for a circular cylinder with a core-shell scattering length density profile. Thus this is a variation of a core-shell cylinder or disc where the shell on the walls and ends may be of different thicknesses and scattering length densities. The form factor is normalized by the particle volume. Schematic cross-section of bicelle. Note however that the model here     calculates for rectangular, not curved, rims as shown below. Cross section of cylindrical symmetry model used here. Users will have    to decide how to distribute "heads" and "tails" between the rim, face    and core regions in order to estimate appropriate starting parameters. Given the scattering length densities (sld) $\rho_c$, the core sld, $\rho_f$, the face sld, $\rho_r$, the rim sld and $\rho_s$ the solvent sld, the scattering length density variation along the cylinder axis is: $$  \rho(r) = \begin{cases} rho_c \text{ for } 0 \lt r \lt R; -L \lt z\lt L \\[1.5ex] rho_f \text{ for } 0 \lt r \lt R; -(L+2t) \lt z\lt -L; L \lt z\lt (L+2t) \\[1.5ex] rho_r\text{ for } 0 \lt r \lt R; -(L+2t) \lt z\lt -L; L \lt z\lt (L+2t) \end{cases} $$ The form factor for the bicelle is calculated in cylindrical coordinates, where $\alpha$ is the angle between the $Q$ vector and the cylinder axis, to give: $$  I(Q,\alpha) = \frac{\text{scale}}{V_t} \cdot F(Q,\alpha)^2 \cdot sin(\alpha) + \text{background} $$ where $$  \begin{align*} F(Q,\alpha) = bigg[ (\rho_c - \rho_f) V_c \frac{2J_1(QRsin \alpha)}{QRsin\alpha} \frac{sin(QLcos\alpha/2)}{Q(L/2)cos\alpha} \\ &+(\rho_f - \rho_r) V_{c+f} \frac{2J_1(QRsin\alpha)}{QRsin\alpha} \frac{sin(Q(L/2+t_f)cos\alpha)}{Q(L/2+t_f)cos\alpha} \\ &+(\rho_r - \rho_s) V_t \frac{2J_1(Q(R+t_r)sin\alpha)}{Q(R+t_r)sin\alpha} \frac{sin(Q(L/2+t_f)cos\alpha)}{Q(L/2+t_f)cos\alpha} \bigg] \end{align*} $$ where $V_t$ is the total volume of the bicelle, $V_c$ the volume of the core, $V_{c+f}$ the volume of the core plus the volume of the faces, $R$ is the radius of the core, $L$ the length of the core, $t_f$ the thickness of the face, $t_r$ the thickness of the rim and $J_1$ the usual first order Bessel function. The output of the 1D scattering intensity function for randomly oriented cylinders is then given by integrating over all possible $\theta$ and $\phi$. For oriented bicelles the *theta*, and *phi* orientation parameters will appear when fitting 2D data, see the `cylinder` model for further information. Our implementation of the scattering kernel and the 1D scattering intensity use the c-library from NIST. Definition of the angles for the oriented core shell bicelle model,     note that the cylinder axis of the bicelle starts along the beam direction     when $\theta  = \phi = 0$. References #. D Singh (2009). *Small angle scattering studies of self assembly in    lipid mixtures*, John's Hopkins University Thesis (2009) 223-225. `Available    from Proquest <http://search.proquest.com/docview/304915826>`_ #.  L. Onsager, *Ann. New York Acad. Sci.*, 51 (1949) 627-659 Authorship and Verification **Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Paul Butler **Date:** September 30, 2016 **Last Reviewed by:** Richard Heenan **Date:** January 4, 2017

Definition

This model provides the form factor for a circular cylinder with a core-shell scattering length density profile. Thus this is a variation of a core-shell cylinder or disc where the shell on the walls and ends may be of different thicknesses and scattering length densities. The form factor is normalized by the particle volume.

Schematic cross-section of bicelle. Note however that the model here     calculates for rectangular, not curved, rims as shown below.

Cross section of cylindrical symmetry model used here. Users will have    to decide how to distribute "heads" and "tails" between the rim, face    and core regions in order to estimate appropriate starting parameters.

Given the scattering length densities (sld) $\rho_c$, the core sld, $\rho_f$, the face sld, $\rho_r$, the rim sld and $\rho_s$ the solvent sld, the scattering length density variation along the cylinder axis is:

$$  \rho(r) = \begin{cases} rho_c \text{ for } 0 \lt r \lt R; -L \lt z\lt L \\[1.5ex] rho_f \text{ for } 0 \lt r \lt R; -(L+2t) \lt z\lt -L; L \lt z\lt (L+2t) \\[1.5ex] rho_r\text{ for } 0 \lt r \lt R; -(L+2t) \lt z\lt -L; L \lt z\lt (L+2t) \end{cases} $$ The form factor for the bicelle is calculated in cylindrical coordinates, where $\alpha$ is the angle between the $Q$ vector and the cylinder axis, to give:

$$  I(Q,\alpha) = \frac{\text{scale}}{V_t} \cdot F(Q,\alpha)^2 \cdot sin(\alpha) + \text{background} $$ where

$$  \begin{align*} F(Q,\alpha) = bigg[ (\rho_c - \rho_f) V_c \frac{2J_1(QRsin \alpha)}{QRsin\alpha} \frac{sin(QLcos\alpha/2)}{Q(L/2)cos\alpha} \\ &+(\rho_f - \rho_r) V_{c+f} \frac{2J_1(QRsin\alpha)}{QRsin\alpha} \frac{sin(Q(L/2+t_f)cos\alpha)}{Q(L/2+t_f)cos\alpha} \\ &+(\rho_r - \rho_s) V_t \frac{2J_1(Q(R+t_r)sin\alpha)}{Q(R+t_r)sin\alpha} \frac{sin(Q(L/2+t_f)cos\alpha)}{Q(L/2+t_f)cos\alpha} \bigg] \end{align*} $$ where $V_t$ is the total volume of the bicelle, $V_c$ the volume of the core, $V_{c+f}$ the volume of the core plus the volume of the faces, $R$ is the radius of the core, $L$ the length of the core, $t_f$ the thickness of the face, $t_r$ the thickness of the rim and $J_1$ the usual first order Bessel function.

The output of the 1D scattering intensity function for randomly oriented cylinders is then given by integrating over all possible $\theta$ and $\phi$.

For oriented bicelles the *theta*, and *phi* orientation parameters will appear when fitting 2D data, see the `cylinder` model for further information. Our implementation of the scattering kernel and the 1D scattering intensity use the c-library from NIST.

Definition of the angles for the oriented core shell bicelle model,     note that the cylinder axis of the bicelle starts along the beam direction     when $\theta  = \phi = 0$.

References

#. D Singh (2009). *Small angle scattering studies of self assembly in    lipid mixtures*, John's Hopkins University Thesis (2009) 223-225. `Available    from Proquest <http://search.proquest.com/docview/304915826>`_

#.  L. Onsager, *Ann. New York Acad. Sci.*, 51 (1949) 627-659

Authorship and Verification

**Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Paul Butler **Date:** September 30, 2016 **Last Reviewed by:** Richard Heenan **Date:** January 4, 2017

Source: https://marketplace.sasview.org/models/64/
