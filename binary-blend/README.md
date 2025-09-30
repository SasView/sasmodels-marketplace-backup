# Binary Blend

Two-polymer RPA model with a flat background. Definition ------------ This model calculates the scattering from a two polymer blend using the Random Phase Approximation (RPA). This is a revision of the $binary$ $blend$ model posted to the Marketplace in May 2020 following User feedback. NOTE: The two polymers are assumed to be monodisperse and incompressible. The scattered intensity $I(q)$ is calculated as[1,2] $$ \frac {(\rho_A - \rho_B)^2}{N_{Av} \cdot I(q)} = scale \cdot [\frac {1}{\phi_A \cdot n_A \cdot v_A \cdot P_A(q)} + \frac {1}{\phi_B \cdot n_B \cdot v_B \cdot P_B(q)} - \frac {2 \cdot \chi_{AB}}{v_0}] + background $$ where $\rho_i$ is the scattering length density, $\phi_i$, is the volume fraction (such that $\phi_A$ + $\phi_B$ = 1), $n_i$ is the degree of polymerization (number of repeat units), $v_i$ is the molar specific volume of one $monomer$, and $P_i(q)$ is Debye's Gaussian coil form factor for polymer $i$, $N_{Av}$ is Avogadro's number, $\chi_{AB}$ is the Flory-Huggins interaction parameter and $v_0$ is the reference volume, and $$ v_i = m_i / \delta_i $$ $$ v_0 = sqrt(v_A \cdot v_B) $$ $$ Z = (q \cdot Rg_i)^2 \ $$ $$ P_i(q) = 2 \cdot [exp(-Z) + Z - 1] / Z^2 $$ where $m_i$ is the molecular weight of a $repeat$ $unit$ (not of the polymer), $\delta_i$ is the mass density, and $Rg_i$ is the radius of gyration of polymer $i$. NOTE: This model works best when as few parameters as possible are allowed to optimize. Indeed, most parameters should be known $a$ $priori$ anyhow! The calculation should also be exact, meaning the $scale$ parameter should be left at 1. TIP: Try alternately optimizing $n_A$ & $rg_A$ and $n_B$ & $rg_B$ and only then optimizing $\chi_{AB}$. Acknowledgments ------------------------ The author would like to thank James Cresswell and Richard Thompson for highlighting some issues with the model as it was originally coded. The molar specific volumes were being computed from the polymer molecular weight, not the weight of the repeat unit, meaning in most instances the values were grossly over-estimated, whilst the reference volume was fixed at a value which in most instances would have been too small. Both issues are corrected in this version of the model. References --------------- 1.  Lapp, Picot & Benoit, $Macromolecules$, (1985), 18, 2437-2441 (Appendix) 2.  Hammouda, $The$ $SANS$ $Toolbox$, Chapters 28, 29 & 34 and Section H Authorship and Verification ------------------------------------ Author: Steve King  Date: 07/05/2020 Last Modified by: Steve King  Date: 12/09/2024 Last Reviewed by:  Date:

Two-polymer RPA model with a flat background.

Definition ------------ This model calculates the scattering from a two polymer blend using the Random Phase Approximation (RPA).

This is a revision of the $binary$ $blend$ model posted to the Marketplace in May 2020 following User feedback.

NOTE: The two polymers are assumed to be monodisperse and incompressible.

The scattered intensity $I(q)$ is calculated as[1,2]

$$ \frac {(\rho_A - \rho_B)^2}{N_{Av} \cdot I(q)} = scale \cdot [\frac {1}{\phi_A \cdot n_A \cdot v_A \cdot P_A(q)} + \frac {1}{\phi_B \cdot n_B \cdot v_B \cdot P_B(q)} - \frac {2 \cdot \chi_{AB}}{v_0}] + background $$

where $\rho_i$ is the scattering length density, $\phi_i$, is the volume fraction (such that $\phi_A$ + $\phi_B$ = 1), $n_i$ is the degree of polymerization (number of repeat units), $v_i$ is the molar specific volume of one $monomer$, and $P_i(q)$ is Debye's Gaussian coil form factor for polymer $i$, $N_{Av}$ is Avogadro's number, $\chi_{AB}$ is the Flory-Huggins interaction parameter and $v_0$ is the reference volume,

and

$$ v_i = m_i / \delta_i $$ $$ v_0 = sqrt(v_A \cdot v_B) $$ $$ Z = (q \cdot Rg_i)^2 \ $$ $$ P_i(q) = 2 \cdot [exp(-Z) + Z - 1] / Z^2 $$

where $m_i$ is the molecular weight of a $repeat$ $unit$ (not of the polymer), $\delta_i$ is the mass density, and $Rg_i$ is the radius of gyration of polymer $i$.

NOTE: This model works best when as few parameters as possible are allowed to optimize. Indeed, most parameters should be known $a$ $priori$ anyhow! The calculation should also be exact, meaning the $scale$ parameter should be left at 1.

TIP: Try alternately optimizing $n_A$ & $rg_A$ and $n_B$ & $rg_B$ and only then optimizing $\chi_{AB}$.

Acknowledgments ------------------------ The author would like to thank James Cresswell and Richard Thompson for highlighting some issues with the model as it was originally coded.

The molar specific volumes were being computed from the polymer molecular weight, not the weight of the repeat unit, meaning in most instances the values were grossly over-estimated, whilst the reference volume was fixed at a value which in most instances would have been too small. Both issues are corrected in this version of the model.

References --------------- 1.  Lapp, Picot & Benoit, $Macromolecules$, (1985), 18, 2437-2441 (Appendix) 2.  Hammouda, $The$ $SANS$ $Toolbox$, Chapters 28, 29 & 34 and Section H

Authorship and Verification ------------------------------------ Author: Steve King  Date: 07/05/2020 Last Modified by: Steve King  Date: 12/09/2024 Last Reviewed by:  Date:

Source: https://marketplace.sasview.org/models/124/
