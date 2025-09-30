# Gel Fit

*This model was implemented by an interested user!* Unlike a concentrated polymer solution, the fine-scale polymer distribution in a gel involves at least two characteristic length scales, a shorter correlation length ($\xi$) to describe the rapid fluctuations in the position of the polymer chains that ensure thermodynamic equilibrium (based on an Ornstein-Zernicke, or Lorentz, model), and a longer distance (denoted here as $R_g$) needed to account for the static accumulations of polymer pinned down by junction points or clusters of such points (based on a simple Guinier model). The relative contributions of these two contributions, $I_L(0)$ and $I_G(0)$, are parameterised as *lorentz_scale* and *guinier_scale*, respectively. See also the lorentz model and the gauss_lorentz_gel model. Definition The scattered intensity $I(q)$ is calculated as $$  I(Q) \approx \frac{I_L(0)}{\left(1+\left[(D+1)/3\right]Q^2\xi^2 \right)^{D/2}} + I_G(0) \cdot \exp\left( -Q^2R_{g}^2/3\right) + B $$ Note that the first term reduces to the Ornstein-Zernicke equation when the fractal dimension $D = 2$; ie, when the Flory exponent is 0.5 (theta conditions). In gels with significant hydrogen bonding $D$ has been reported to be ~2.6 to 2.8. References #. Mitsuhiro Shibayama, Toyoichi Tanaka, Charles C Han,    *J. Chem. Phys.* 1992, 97 (9), 6829-6841. DOI: 10.1063/1.463637 #. Simon Mallam, Ferenc Horkay, Anne-Marie Hecht, Adrian R Rennie,    Erik Geissler, *Macromolecules* 1991, 24, 543-548. DOI: 10.1021/MA00002A031 Authorship and Verification **Author:** **Last Modified by:** Steve King **Date:** November 22, 2022 **Last Reviewed by:** Paul Kienzle **Date:** November 21, 2022

*This model was implemented by an interested user!*

Unlike a concentrated polymer solution, the fine-scale polymer distribution in a gel involves at least two characteristic length scales, a shorter correlation length ($\xi$) to describe the rapid fluctuations in the position of the polymer chains that ensure thermodynamic equilibrium (based on an Ornstein-Zernicke, or Lorentz, model), and a longer distance (denoted here as $R_g$) needed to account for the static accumulations of polymer pinned down by junction points or clusters of such points (based on a simple Guinier model). The relative contributions of these two contributions, $I_L(0)$ and $I_G(0)$, are parameterised as *lorentz_scale* and *guinier_scale*, respectively.

See also the lorentz model and the gauss_lorentz_gel model.

Definition

The scattered intensity $I(q)$ is calculated as

$$  I(Q) \approx \frac{I_L(0)}{\left(1+\left[(D+1)/3\right]Q^2\xi^2 \right)^{D/2}} + I_G(0) \cdot \exp\left( -Q^2R_{g}^2/3\right) + B $$ Note that the first term reduces to the Ornstein-Zernicke equation when the fractal dimension $D = 2$; ie, when the Flory exponent is 0.5 (theta conditions). In gels with significant hydrogen bonding $D$ has been reported to be ~2.6 to 2.8.

References

#. Mitsuhiro Shibayama, Toyoichi Tanaka, Charles C Han,    *J. Chem. Phys.* 1992, 97 (9), 6829-6841. DOI: 10.1063/1.463637

#. Simon Mallam, Ferenc Horkay, Anne-Marie Hecht, Adrian R Rennie,    Erik Geissler, *Macromolecules* 1991, 24, 543-548. DOI: 10.1021/MA00002A031

Authorship and Verification

**Author:** **Last Modified by:** Steve King **Date:** November 22, 2022 **Last Reviewed by:** Paul Kienzle **Date:** November 21, 2022

Source: https://marketplace.sasview.org/models/70/
