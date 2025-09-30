# Pearl Necklace

This model provides the form factor for a pearl necklace composed of two elements: *N* pearls (homogeneous spheres of radius *R*) freely jointed by *M* rods (like strings - with a total mass *Mw* = *M* \* *m*`r` + *N* \* *m*\ `s`, and the string segment length (or edge separation) *l* (= *A* - 2*R*)). *A* is the center-to-center pearl separation distance. Pearl Necklace schematic Definition The output of the scattering intensity function for the pearl_necklace is given by (Schweins, 2004) $$  I(q)=\frac{ \text{scale} }{V} \cdot \frac{(S_{ss}(q)+S_{ff}(q)+S_{fs}(q))} {(M \cdot m_f + N \cdot m_s)^2} + \text{bkg} $$ where $$  S_{ss}(q) = 2m_s^2\psi^2(q)\left[\frac{N}{1-sin(qA)/qA}-\frac{N}{2}- \frac{1-(sin(qA)/qA)^N}{(1-sin(qA)/qA)^2}\cdot\frac{sin(qA)}{qA}\right] \\ S_{ff}(q) = m_r^2\left[M\left\{2\Lambda(q)-\left(\frac{sin(ql/2)}{ql/2}\right)\right\}+ \frac{2M\beta^2(q)}{1-sin(qA)/qA}-2\beta^2(q)\cdot \frac{1-(sin(qA)/qA)^M}{(1-sin(qA)/qA)^2}\right] \\ S_{fs}(q) = m_r \beta (q) \cdot m_s \psi (q) \cdot 4\left[ \frac{N-1}{1-sin(qA)/qA}-\frac{1-(sin(qA)/qA)^{N-1}}{(1-sin(qA)/qA)^2} \cdot \frac{sin(qA)}{qA}\right] \\ \psi(q) = 3 \cdot \frac{sin(qR)-(qR)\cdot cos(qR)}{(qR)^3} \\ \Lambda(q) = \frac{\int_0^{ql}\frac{sin(t)}{t}dt}{ql} \\ \beta(q) = \frac{\int_{qR}^{q(A-R)}\frac{sin(t)}{t}dt}{ql} $$ where the mass *m*`i` is (SLD`i` - SLD`solvent`) \* (volume of the *N* pearls/rods). *V* is the total volume of the necklace. .. note:: *num_pearls* must be an integer. The 2D scattering intensity is the same as $P(q)$ above, regardless of the orientation of the *q* vector. References #. R Schweins and K Huber, *Particle Scattering Factor of Pearl Necklace Chains*,    *Macromol. Symp.* 211 (2004) 25-42 2004 #. L. Onsager, *Ann. New York Acad. Sci.*, 51 (1949) 627-659 Authorship and Verification **Author:** **Last Modified by:** Andrew Jackson **Date:** March 28, 2019 **Last Reviewed by:** Steve King **Date:** March 28, 2019

This model provides the form factor for a pearl necklace composed of two elements: *N* pearls (homogeneous spheres of radius *R*) freely jointed by *M* rods (like strings - with a total mass *Mw* = *M* \* *m*`r` + *N* \* *m*\ `s`, and the string segment length (or edge separation) *l* (= *A* - 2*R*)). *A* is the center-to-center pearl separation distance.

Pearl Necklace schematic

Definition

The output of the scattering intensity function for the pearl_necklace is given by (Schweins, 2004)

$$  I(q)=\frac{ \text{scale} }{V} \cdot \frac{(S_{ss}(q)+S_{ff}(q)+S_{fs}(q))} {(M \cdot m_f + N \cdot m_s)^2} + \text{bkg} $$ where

$$  S_{ss}(q) = 2m_s^2\psi^2(q)\left[\frac{N}{1-sin(qA)/qA}-\frac{N}{2}- \frac{1-(sin(qA)/qA)^N}{(1-sin(qA)/qA)^2}\cdot\frac{sin(qA)}{qA}\right] \\ S_{ff}(q) = m_r^2\left[M\left\{2\Lambda(q)-\left(\frac{sin(ql/2)}{ql/2}\right)\right\}+ \frac{2M\beta^2(q)}{1-sin(qA)/qA}-2\beta^2(q)\cdot \frac{1-(sin(qA)/qA)^M}{(1-sin(qA)/qA)^2}\right] \\ S_{fs}(q) = m_r \beta (q) \cdot m_s \psi (q) \cdot 4\left[ \frac{N-1}{1-sin(qA)/qA}-\frac{1-(sin(qA)/qA)^{N-1}}{(1-sin(qA)/qA)^2} \cdot \frac{sin(qA)}{qA}\right] \\ \psi(q) = 3 \cdot \frac{sin(qR)-(qR)\cdot cos(qR)}{(qR)^3} \\ \Lambda(q) = \frac{\int_0^{ql}\frac{sin(t)}{t}dt}{ql} \\ \beta(q) = \frac{\int_{qR}^{q(A-R)}\frac{sin(t)}{t}dt}{ql} $$ where the mass *m*`i` is (SLD`i` - SLD`solvent`) \* (volume of the *N* pearls/rods). *V* is the total volume of the necklace.

.. note::

*num_pearls* must be an integer.

The 2D scattering intensity is the same as $P(q)$ above, regardless of the orientation of the *q* vector.

References

#. R Schweins and K Huber, *Particle Scattering Factor of Pearl Necklace Chains*,    *Macromol. Symp.* 211 (2004) 25-42 2004

#. L. Onsager, *Ann. New York Acad. Sci.*, 51 (1949) 627-659

Authorship and Verification

**Author:** **Last Modified by:** Andrew Jackson **Date:** March 28, 2019 **Last Reviewed by:** Steve King **Date:** March 28, 2019

Source: https://marketplace.sasview.org/models/48/
