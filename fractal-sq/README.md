# Fractal S(q)

Calculates the structure factor term ONLY from the Fractal model. Definition ------------ The Teixeira & Chen fractal structure factor. Calculates the structure factor for mass fractal aggregates of monodisperse spherical particles of effective radius $R_p$ according to \begin{equation} S(q) = 1 + \frac{D_m\Gamma(D_m - 1)}{(qR_p)^{D_m} [1+(q\xi)^{-2}]^{(D_m-1)/2}} sin[(D_m - 1) tan^{-1}(q\xi)] \end{equation} where $D_m$ is the mass fractal dimension, $R_p$ is assumed to be equivalent to the lower fractal cutoff length, and $\xi$ is the upper fractal cutoff length (the distance above which the mass distribution of the fractal no longer scales as $size^{D^m}$). The returned value is a dimensionless structure factor, $S(q)$. The radius-of-gyration for the mass fractal is given by \begin{equation} R_g = \frac{D_m(D_m + 1)\xi^{2}}{2} \end{equation} Unlike most other structure factor models, this $S(q)$ does not explicitly include the particle volume fraction and so the $volfraction$ parameter that SasView adds by default has no effect. If combining this model with a particulate form factor, use the $scale$ parameter to adjust the effective volume fraction. Combining this structure factor model with either the Sphere model or the Core_Shell_Sphere model replicates the Fractal model or the Fractal_Core_Shell model, respectively. In the latter case, make $radius$_$effective$ = $radius$ + $thickness$. The mass fractal dimension, which can be fractional, is only valid in the range $1 <= D_m <= 3$. The S(q) function here goes negative if $D_m$ is too large, and the Gamma function diverges at $D_m$ = 0 and $D_m$ = 1. References --------------- J Teixeira, J. Appl. Cryst., 21 (1988) 781-785 Chapter 6, Equation 6.51 in Small-Angle Scattering from Confined and Interfacial Fluids Yuri B. Melnichenko Springer, 2016 Authorship and Verification ----------------------------------- Author: Ziggy Attala Date: 10/09/2019 Last Modified by: Steve King Date: 19/09/2019 Last Reviewed by: Date:

Calculates the structure factor term ONLY from the Fractal model.

Definition ------------ The Teixeira & Chen fractal structure factor.

Calculates the structure factor for mass fractal aggregates of monodisperse spherical particles of effective radius $R_p$ according to

\begin{equation} S(q) = 1 + \frac{D_m\Gamma(D_m - 1)}{(qR_p)^{D_m} [1+(q\xi)^{-2}]^{(D_m-1)/2}} sin[(D_m - 1) tan^{-1}(q\xi)] \end{equation}

where $D_m$ is the mass fractal dimension, $R_p$ is assumed to be equivalent to the lower fractal cutoff length, and $\xi$ is the upper fractal cutoff length (the distance above which the mass distribution of the fractal no longer scales as $size^{D^m}$).

The returned value is a dimensionless structure factor, $S(q)$.

The radius-of-gyration for the mass fractal is given by

\begin{equation} R_g = \frac{D_m(D_m + 1)\xi^{2}}{2} \end{equation}

Unlike most other structure factor models, this $S(q)$ does not explicitly include the particle volume fraction and so the $volfraction$ parameter that SasView adds by default has no effect. If combining this model with a particulate form factor, use the $scale$ parameter to adjust the effective volume fraction.

Combining this structure factor model with either the Sphere model or the Core_Shell_Sphere model replicates the Fractal model or the Fractal_Core_Shell model, respectively. In the latter case, make $radius$_$effective$ = $radius$ + $thickness$.

The mass fractal dimension, which can be fractional, is only valid in the range $1 <= D_m <= 3$. The S(q) function here goes negative if $D_m$ is too large, and the Gamma function diverges at $D_m$ = 0 and $D_m$ = 1.

References --------------- J Teixeira, J. Appl. Cryst., 21 (1988) 781-785

Chapter 6, Equation 6.51 in Small-Angle Scattering from Confined and Interfacial Fluids Yuri B. Melnichenko Springer, 2016

Authorship and Verification ----------------------------------- Author: Ziggy Attala Date: 10/09/2019 Last Modified by: Steve King Date: 19/09/2019 Last Reviewed by: Date:

Source: https://marketplace.sasview.org/models/119/
