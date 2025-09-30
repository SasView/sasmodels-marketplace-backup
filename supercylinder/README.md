# Supercylinder

## Definition This supercylinder model is an implementation based on Maric $\textit{et al}$, 2017 (#reference-1). Its shape can be described by a superellipsoid (Barr, 1992 (#reference-2) as: $$\left(\left| x \right|^{2} + \left| y \right|^{2}\right)^{t/2} + \left|\frac{ z}{\epsilon}\right|^t \leq |R|^t$$ Setting $|r|^2 = \left| x \right|^{2} + \left| y \right|^{2}$, the radius $r$ of the superellisoid at a $z$ value can be related as: $$r(z) = \left|R^t - \left|\frac{z}{\epsilon}\right|^t\right|^{1/t}$$ Where, $R$ is the radius at the equator, $\epsilon$ is the eccentricity and $t$ is the superellipticity. The supercylinder model is based on the form factor amplitude for a cylinder with length $2R_{cyl}\epsilon$ and radius $R_{cyl}$: $$F(q) = 2 \Delta \rho V \frac{\sin\left(\frac{1}{2} q (2 R_{cyl}\epsilon)\cos\theta\right) J_1\left(q R_{cyl} \sin\theta\right)}{\frac{1}{2}q (2R_{cyl}\epsilon) \cos\theta \ \ \ q R_{cyl} \sin\theta}$$ where $V$ is the volume of the supercylinder, $\Delta\rho$ is the contrast between the solvents and the particles scattering length density, and $J_1$ is the first order Bessel function of first kind. If the radius is $R_{cyl} = r(z)$ such that it changes with $z$, the small cylinders must all be integrated over the length of the cylinder. $$ F(q) = 2 \Delta \rho V \frac{\sin\left(q R_{cyl}\epsilon\cos\theta\right) J_1\left(q R_{cyl} \sin\theta\right)}{q R_{cyl}\epsilon \cos\theta \ \ \ q R_{cyl} \sin\theta}\\ $$ $$ = 2 \int_0^{R \epsilon} 2 \Delta \rho \pi r(z)^2 \frac{J_1\left(q r(z) \sin\theta\right)}{q \cos\theta \ \ \ q r(z) \sin\theta} \cos\left(q z\cos\theta\right) q \cos\theta \ dz\\ $$ $$ =  \int_0^{R \epsilon} 4 \Delta \rho \pi r(z) \frac{J_1\left(q r(z) \sin\theta\right)}{q \sin\theta} \cos\left(q z\cos\theta\right) \ dz $$ Given randomly oriented particles, the form factor can be written as: $$P(q) = \int^{\pi / 2}_0 \left| \int_0^{R\epsilon} 4 \Delta \rho \pi \epsilon r(z) \frac{\cos\left( q  r(z)\cos\theta\right) J_1\left(q z\sin\theta\right)}{q \sin\theta} \ dz \right|^2 \sin\theta \ d\theta$$ which is solved numerically. Thus, the supercylinder model is given as: $$I(q) = \text{scale}  \ P(q) + \text{background}$$ ## Validation The model is validated by using Shape2SAS (Larsen $\textit{et al}$, 2023 (#reference-3) to numerically generate simulated SAXS data for different supercylinders and fitting these with the model. This has been done in the range of $R \in [50, 100]$, $t \in [0.2, 50]$ and $\epsilon \in [0.5, 1.5]$. In these ranges, the model is found to be stable. ## References 1. Maric, Selma & Lind, Tania & Lyngsø, Jeppe & Cárdenas, Marité & Pedersen, Jan. (2017). Modeling Small-Angle X-Ray Scattering Data for Low Density Lipoproteins – Insights Into The Fatty Core Phase Packing And Transition. ACS Nano. 11. 10.1021/acsnano.6b08089. 2. A.H. Barr, III. 8-RIGID PHYSICALLY BASED SUPERQUADRICS, Editor(s): DAVID KIRK, Graphics Gems III (IBM Version), Morgan Kaufmann, 1992, Pages 137-159, ISBN 9780124096738, https://doi.org/10.1016/B978-0-08-050755-2.50038-5. 3. Larsen, A. H., Brookes, E., Pedersen, M. C. & Kirkensgaard, J. J. K. (2023). Shape2SAS: a web application to simulate small-angle scattering data and pair distance distributions from user-defined shapes. Journal of Applied Crystallography 56, 1287-1294. [https://doi.org/10.1107/S1600576723005848](https://doi.org/10.1107/S1600576723005848)

## Definition

This supercylinder model is an implementation based on Maric $\textit{et al}$, 2017 (#reference-1). Its shape can be described by a superellipsoid (Barr, 1992 (#reference-2) as:

$$\left(\left| x \right|^{2} + \left| y \right|^{2}\right)^{t/2} + \left|\frac{ z}{\epsilon}\right|^t \leq |R|^t$$

Setting $|r|^2 = \left| x \right|^{2} + \left| y \right|^{2}$, the radius $r$ of the superellisoid at a $z$ value can be related as:

$$r(z) = \left|R^t - \left|\frac{z}{\epsilon}\right|^t\right|^{1/t}$$

Where, $R$ is the radius at the equator, $\epsilon$ is the eccentricity and $t$ is the superellipticity.

The supercylinder model is based on the form factor amplitude for a cylinder with length $2R_{cyl}\epsilon$ and radius $R_{cyl}$:

$$F(q) = 2 \Delta \rho V \frac{\sin\left(\frac{1}{2} q (2 R_{cyl}\epsilon)\cos\theta\right) J_1\left(q R_{cyl} \sin\theta\right)}{\frac{1}{2}q (2R_{cyl}\epsilon) \cos\theta \ \ \ q R_{cyl} \sin\theta}$$

where $V$ is the volume of the supercylinder, $\Delta\rho$ is the contrast between the solvents and the particles scattering length density, and $J_1$ is the first order Bessel function of first kind.

If the radius is $R_{cyl} = r(z)$ such that it changes with $z$, the small cylinders must all be integrated over the length of the cylinder.

$$ F(q) = 2 \Delta \rho V \frac{\sin\left(q R_{cyl}\epsilon\cos\theta\right) J_1\left(q R_{cyl} \sin\theta\right)}{q R_{cyl}\epsilon \cos\theta \ \ \ q R_{cyl} \sin\theta}\\ $$

$$ = 2 \int_0^{R \epsilon} 2 \Delta \rho \pi r(z)^2 \frac{J_1\left(q r(z) \sin\theta\right)}{q \cos\theta \ \ \ q r(z) \sin\theta} \cos\left(q z\cos\theta\right) q \cos\theta \ dz\\ $$

$$ =  \int_0^{R \epsilon} 4 \Delta \rho \pi r(z) \frac{J_1\left(q r(z) \sin\theta\right)}{q \sin\theta} \cos\left(q z\cos\theta\right) \ dz $$ Given randomly oriented particles, the form factor can be written as:

$$P(q) = \int^{\pi / 2}_0 \left| \int_0^{R\epsilon} 4 \Delta \rho \pi \epsilon r(z) \frac{\cos\left( q  r(z)\cos\theta\right) J_1\left(q z\sin\theta\right)}{q \sin\theta} \ dz \right|^2 \sin\theta \ d\theta$$

which is solved numerically. Thus, the supercylinder model is given as:

$$I(q) = \text{scale}  \ P(q) + \text{background}$$

## Validation

The model is validated by using Shape2SAS (Larsen $\textit{et al}$, 2023 (#reference-3) to numerically generate simulated SAXS data for different supercylinders and fitting these with the model. This has been done in the range of $R \in [50, 100]$, $t \in [0.2, 50]$ and $\epsilon \in [0.5, 1.5]$. In these ranges, the model is found to be stable.

## References

1. Maric, Selma & Lind, Tania & Lyngsø, Jeppe & Cárdenas, Marité & Pedersen, Jan. (2017). Modeling Small-Angle X-Ray Scattering Data for Low Density Lipoproteins – Insights Into The Fatty Core Phase Packing And Transition. ACS Nano. 11. 10.1021/acsnano.6b08089.

2. A.H. Barr, III. 8-RIGID PHYSICALLY BASED SUPERQUADRICS, Editor(s): DAVID KIRK, Graphics Gems III (IBM Version), Morgan Kaufmann, 1992, Pages 137-159, ISBN 9780124096738, https://doi.org/10.1016/B978-0-08-050755-2.50038-5.

3. Larsen, A. H., Brookes, E., Pedersen, M. C. & Kirkensgaard, J. J. K. (2023). Shape2SAS: a web application to simulate small-angle scattering data and pair distance distributions from user-defined shapes. Journal of Applied Crystallography 56, 1287-1294. [https://doi.org/10.1107/S1600576723005848](https://doi.org/10.1107/S1600576723005848)

# Example Data:

Source: https://marketplace.sasview.org/models/164/
