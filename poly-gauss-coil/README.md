# Poly Gauss Coil

#poly_gauss_coil model #conversion of Poly_GaussCoil.py #converted by Steve King, Mar 2016 This empirical model describes the scattering from *polydisperse* polymer chains in theta solvents or polymer melts, assuming a Schulz-Zimm type molecular weight distribution. To describe the scattering from *monodisperse* polymer chains, see the `mono-gauss-coil` model. Definition $$  I(q) = \text{scale} \cdot I_0 \cdot P(q) + \text{background} $$ where $$  I_0 = \phi_\text{poly} \cdot V \cdot (\rho_\text{poly}-\rho_\text{solv})^2 \\ P(q) = 2 [(1 + UZ)^{-1/U} + Z - 1] / [(1 + U) Z^2] \\ Z = [(q R_g)^2] / (1 + 2U) \\ U = (Mw / Mn) - 1 = \text{polydispersity ratio} - 1 \\ V = M / (N_A \delta) $$ Here, $\phi_\text{poly}$, is the volume fraction of polymer, $V$ is the volume of a polymer coil, $M$ is the molecular weight of the polymer, $N_A$ is Avogadro's Number, $\delta$ is the bulk density of the polymer, $\rho_\text{poly}$ is the sld of the polymer, $\rho_\text{solv}$ is the sld of the solvent, and $R_g$ is the radius of gyration of the polymer coil. The 2D scattering intensity is calculated in the same way as the 1D, but where the $q$ vector is redefined as $$  q = \sqrt{q_x^2 + q_y^2} $$ References #. O Glatter and O Kratky (editors), *Small Angle X-ray Scattering*,    Academic Press, (1982) Page 404 #. J S Higgins, H C Benoit, *Polymers and Neutron Scattering*,    Oxford Science Publications, (1996) #. S M King, *Small Angle Neutron Scattering*    in *Modern Techniques for Polymer Characterisation*, Wiley, (1999) #. http://www.ncnr.nist.gov/staff/hammouda/distance_learning/chapter_28.pdf Authorship and Verification **Author:** **Last Modified by:** **Last Reviewed by:**

#poly_gauss_coil model #conversion of Poly_GaussCoil.py #converted by Steve King, Mar 2016 This empirical model describes the scattering from *polydisperse* polymer chains in theta solvents or polymer melts, assuming a Schulz-Zimm type molecular weight distribution.

To describe the scattering from *monodisperse* polymer chains, see the `mono-gauss-coil` model.

Definition

$$  I(q) = \text{scale} \cdot I_0 \cdot P(q) + \text{background} $$ where

$$  I_0 = \phi_\text{poly} \cdot V \cdot (\rho_\text{poly}-\rho_\text{solv})^2 \\ P(q) = 2 [(1 + UZ)^{-1/U} + Z - 1] / [(1 + U) Z^2] \\ Z = [(q R_g)^2] / (1 + 2U) \\ U = (Mw / Mn) - 1 = \text{polydispersity ratio} - 1 \\ V = M / (N_A \delta) $$ Here, $\phi_\text{poly}$, is the volume fraction of polymer, $V$ is the volume of a polymer coil, $M$ is the molecular weight of the polymer, $N_A$ is Avogadro's Number, $\delta$ is the bulk density of the polymer, $\rho_\text{poly}$ is the sld of the polymer, $\rho_\text{solv}$ is the sld of the solvent, and $R_g$ is the radius of gyration of the polymer coil.

The 2D scattering intensity is calculated in the same way as the 1D, but where the $q$ vector is redefined as

$$  q = \sqrt{q_x^2 + q_y^2} $$ References

#. O Glatter and O Kratky (editors), *Small Angle X-ray Scattering*,    Academic Press, (1982) Page 404 #. J S Higgins, H C Benoit, *Polymers and Neutron Scattering*,    Oxford Science Publications, (1996) #. S M King, *Small Angle Neutron Scattering*    in *Modern Techniques for Polymer Characterisation*, Wiley, (1999) #. http://www.ncnr.nist.gov/staff/hammouda/distance_learning/chapter_28.pdf

Authorship and Verification

**Author:** **Last Modified by:** **Last Reviewed by:**

Source: https://marketplace.sasview.org/models/37/
