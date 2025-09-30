# Mass Fractal S(q)

Calculates the structure factor term ONLY from the Mass Fractal model. Definition ---------- The Sinha-Mildner-Hall fractal structure factor. The functional form of the structure factor is defined below \begin{equation} S(q) = \frac{\Gamma(D_m-1)\xi^{D_m-1}}{\left[1+(q\xi)^2 \right]^{(D_m-1)/2}} \frac{sin\left[(D_m - 1) tan^{-1}(q\xi) \right]}{q} \end{equation} where $D_m$ is the $mass$ fractal dimension and $\xi$ is the upper fractal cutoff length, i.e. the length scale above which the system is no longer fractal. SasView automatically appends two additional parameters $radius$_$effective$ and $volfraction$ to all $S(q)$ models. However, these are not used by this model. The mass fractal dimension ( $D_m$ ) is only valid if $1 <= D_m <= 3$. It is also only valid over a limited $q$ range (see the references for details). WARNING! By convention, $S(q)$ is normally dimensionless. THIS FUNCTION IS NOT DIMENSIONLESS! References --------------- D Mildner and P Hall, J. Phys. D: Appl. Phys., 19 (1986) 1535-1545 Equation(9) P Wong, Methods in the physics of porous media San Diego; London. Academic. (1999) Authorship and Verification ----------------------------------- Author: Ziggy Attala and Matt D G Hughes Date: 09/09/2019 Last Modified by: Steve King Date: 18/09/2019 Last Reviewed by:

Calculates the structure factor term ONLY from the Mass Fractal model.

Definition ---------- The Sinha-Mildner-Hall fractal structure factor.

The functional form of the structure factor is defined below

\begin{equation} S(q) = \frac{\Gamma(D_m-1)\xi^{D_m-1}}{\left[1+(q\xi)^2 \right]^{(D_m-1)/2}} \frac{sin\left[(D_m - 1) tan^{-1}(q\xi) \right]}{q} \end{equation}

where $D_m$ is the $mass$ fractal dimension and $\xi$ is the upper fractal cutoff length, i.e. the length scale above which the system is no longer fractal.

SasView automatically appends two additional parameters $radius$_$effective$ and $volfraction$ to all $S(q)$ models. However, these are not used by this model.

The mass fractal dimension ( $D_m$ ) is only valid if $1 <= D_m <= 3$. It is also only valid over a limited $q$ range (see the references for details).

WARNING! By convention, $S(q)$ is normally dimensionless. THIS FUNCTION IS NOT DIMENSIONLESS!

References --------------- D Mildner and P Hall, J. Phys. D: Appl. Phys., 19 (1986) 1535-1545 Equation(9)

P Wong, Methods in the physics of porous media San Diego; London. Academic. (1999)

Authorship and Verification ----------------------------------- Author: Ziggy Attala and Matt D G Hughes Date: 09/09/2019 Last Modified by: Steve King Date: 18/09/2019 Last Reviewed by:

Source: https://marketplace.sasview.org/models/118/
