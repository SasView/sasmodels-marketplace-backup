# Linear Pearls

This model provides the form factor for $N$ spherical pearls of radius $R$ linearly joined by short strings (or segment length or edge separation) $l$ $(= A - 2R)$. $A$ is the center-to-center pearl separation distance. The thickness of each string is assumed to be negligible. Definition The output of the scattering intensity function for the linear_pearls model is given by (Dobrynin, 1996) $$  P(Q) = \frac{\text{scale}}{V}\left[ m_{p}^2 \left(N+2\sum_{n-1}^{N-1}(N-n)\frac{\sin(qnl)}{qnl}\right) \left( 3\frac{\sin(qR)-qR\cos(qR)}{(qr)^3}\right)^2\right] $$ where the mass $m_p$ is $(SLD_{pearl}-SLD_{solvent})*(volumeofNpearls)$. V is the total volume. The 2D scattering intensity is the same as P(q) above, regardless of the orientation of the q vector. References #.  A V Dobrynin, M Rubinstein and S P Obukhov, *Macromol.*, 29 (1996) 2974-2979 Authorship and Verification **Author:** **Last Modified by:** **Last Reviewed by:**

This model provides the form factor for $N$ spherical pearls of radius $R$ linearly joined by short strings (or segment length or edge separation) $l$ $(= A - 2R)$. $A$ is the center-to-center pearl separation distance. The thickness of each string is assumed to be negligible.

Definition

The output of the scattering intensity function for the linear_pearls model is given by (Dobrynin, 1996)

$$  P(Q) = \frac{\text{scale}}{V}\left[ m_{p}^2 \left(N+2\sum_{n-1}^{N-1}(N-n)\frac{\sin(qnl)}{qnl}\right) \left( 3\frac{\sin(qR)-qR\cos(qR)}{(qr)^3}\right)^2\right] $$ where the mass $m_p$ is $(SLD_{pearl}-SLD_{solvent})*(volumeofNpearls)$. V is the total volume.

The 2D scattering intensity is the same as P(q) above, regardless of the orientation of the q vector.

References

#.  A V Dobrynin, M Rubinstein and S P Obukhov, *Macromol.*, 29 (1996) 2974-2979

Authorship and Verification

**Author:** **Last Modified by:** **Last Reviewed by:**

Source: https://marketplace.sasview.org/models/78/
