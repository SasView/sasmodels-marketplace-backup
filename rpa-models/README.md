# RPA models

Calculates the macroscopic scattering intensity for a multi-component homogeneous mixture of polymers using the Random Phase Approximation. This general formalism contains 10 specific cases Case 0: C/D binary mixture of homopolymers Case 1: C-D diblock copolymer Case 2: B/C/D ternary mixture of homopolymers Case 3: C/C-D mixture of a homopolymer B and a diblock copolymer C-D Case 4: B-C-D triblock copolymer Case 5: A/B/C/D quaternary mixture of homopolymers Case 6: A/B/C-D mixture of two homopolymers A/B and a diblock C-D Case 7: A/B-C-D mixture of a homopolymer A and a triblock B-C-D Case 8: A-B/C-D mixture of two diblock copolymers A-B and C-D Case 9: A-B-C-D tetra-block copolymer **NB: these case numbers are different from those in the NIST SANS package!** Only one case can be used at any one time. The RPA (mean field) formalism only applies only when the multicomponent polymer mixture is in the homogeneous mixed-phase region. **Component D is assumed to be the "background" component (ie, all contrasts are calculated with respect to component D).** So the scattering contrast for a C/D blend = [SLD(component C) - SLD(component D)]$^2$. Depending on which case is being used, the number of fitting parameters - the segment lengths (ba, bb, etc) and $\chi$ parameters (Kab, Kac, etc) - vary. The *scale* parameter should be held equal to unity. The input parameters are the degrees of polymerization, the volume fractions, the specific volumes, and the neutron scattering length densities for each component. References ---------- A Z Akcasu, R Klein and B Hammouda, *Macromolecules*, 26 (1993) 4136

Calculates the macroscopic scattering intensity for a multi-component homogeneous mixture of polymers using the Random Phase Approximation. This general formalism contains 10 specific cases

Case 0: C/D binary mixture of homopolymers

Case 1: C-D diblock copolymer

Case 2: B/C/D ternary mixture of homopolymers

Case 3: C/C-D mixture of a homopolymer B and a diblock copolymer C-D

Case 4: B-C-D triblock copolymer

Case 5: A/B/C/D quaternary mixture of homopolymers

Case 6: A/B/C-D mixture of two homopolymers A/B and a diblock C-D

Case 7: A/B-C-D mixture of a homopolymer A and a triblock B-C-D

Case 8: A-B/C-D mixture of two diblock copolymers A-B and C-D

Case 9: A-B-C-D tetra-block copolymer

**NB: these case numbers are different from those in the NIST SANS package!**

Only one case can be used at any one time.

The RPA (mean field) formalism only applies only when the multicomponent polymer mixture is in the homogeneous mixed-phase region.

**Component D is assumed to be the "background" component (ie, all contrasts are calculated with respect to component D).** So the scattering contrast for a C/D blend = [SLD(component C) - SLD(component D)]$^2$.

Depending on which case is being used, the number of fitting parameters - the segment lengths (ba, bb, etc) and $\chi$ parameters (Kab, Kac, etc) - vary. The *scale* parameter should be held equal to unity.

The input parameters are the degrees of polymerization, the volume fractions, the specific volumes, and the neutron scattering length densities for each component.

References ----------

A Z Akcasu, R Klein and B Hammouda, *Macromolecules*, 26 (1993) 4136

# Example Data:

Source: https://marketplace.sasview.org/models/5/
