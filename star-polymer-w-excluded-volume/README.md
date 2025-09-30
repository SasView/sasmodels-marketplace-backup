# Star Polymer w/ Excluded Volume

This model describes scattering from a star-branched polymer where the arms of the polymer may have excluded volume, i.e., they need not be Gaussian chains. Under this model, the form factor of the star polymer with $f$ arms having degree of polymerization $N$ is given by $$ P_{star}(q) = \frac{1}{f^{2}} \left[ fP_{sb}(q,N) + f(f-1)P_{ib}(q,N) \right] $$ $P_{sb}(q,N)$ is the single branch/arm form factor, given by: $$ P_{sb}(q,N) = \frac{1}{\nu U^{1/2\nu}}\gamma\left( \frac{1}{2v}, U \right) - \frac{1}{\nu U^{1/\nu}}\gamma\left( \frac{1}{\nu}, U\right) $$ where $\nu$ is the excluded volume parameter, $U = q^{2}b^{2}N^{2\nu}/6$ and $b$ is the Kuhn length. The interbranch/arm form factor is given by: $$ P_{ib}(q,N) = 2P_{sb}(q,2N) - P_{sb}(q,N) $$ The final scattering intensity that this model gives is $$ I(q) = scale \times (\rho_{P} - \rho_{S})^{2}P_{star}(q) + B $$ where $\rho_{P}$ and $\rho_{S}$ are the scattering length densities of the polymer and solvent, respectively, and $B$ is the incoherent background. ----- References 1. B. Hammouda, "Form Factors for Branched Polymers with Excluded Volume", J. of Research of NIST, 121, 139-164 (2016). 2. X. Lang, W. R. Lenart, J. E. P. Sun, B. Hammouda, and M. J. A. Hore, "Interaction and Conformation of Aqueous Poly(N-isopropylacrylamide) (PNIPAM) Star Polymers below the LCST", Macromolecules, 50, 2145-2154 (2017).

This model describes scattering from a star-branched polymer where the arms of the polymer may have excluded volume, i.e., they need not be Gaussian chains.

Under this model, the form factor of the star polymer with $f$ arms having degree of polymerization $N$ is given by

$$ P_{star}(q) = \frac{1}{f^{2}} \left[ fP_{sb}(q,N) + f(f-1)P_{ib}(q,N) \right] $$ $P_{sb}(q,N)$ is the single branch/arm form factor, given by: $$ P_{sb}(q,N) = \frac{1}{\nu U^{1/2\nu}}\gamma\left( \frac{1}{2v}, U \right) - \frac{1}{\nu U^{1/\nu}}\gamma\left( \frac{1}{\nu}, U\right) $$ where $\nu$ is the excluded volume parameter, $U = q^{2}b^{2}N^{2\nu}/6$ and $b$ is the Kuhn length. The interbranch/arm form factor is given by: $$ P_{ib}(q,N) = 2P_{sb}(q,2N) - P_{sb}(q,N) $$

The final scattering intensity that this model gives is $$ I(q) = scale \times (\rho_{P} - \rho_{S})^{2}P_{star}(q) + B $$ where $\rho_{P}$ and $\rho_{S}$ are the scattering length densities of the polymer and solvent, respectively, and $B$ is the incoherent background.

----- References

1. B. Hammouda, "Form Factors for Branched Polymers with Excluded Volume", J. of Research of NIST, 121, 139-164 (2016).

2. X. Lang, W. R. Lenart, J. E. P. Sun, B. Hammouda, and M. J. A. Hore, "Interaction and Conformation of Aqueous Poly(N-isopropylacrylamide) (PNIPAM) Star Polymers below the LCST", Macromolecules, 50, 2145-2154 (2017).

# Example Data:

Source: https://marketplace.sasview.org/models/102/
