# Pringle-Schmidt Helices

This is the Pringle-Schmidt equation for fitting the helical form factor of an infinitely long helix formed from two helical tapes wrapped around each other at an angle $\epsilon$. The two helices are assumed to have the same width and thickness. Please see Figure 1 in Reference [1]. Note that this figure uses $\phi$ in place of the $\epsilon$ used here (because $\phi$ has another meaning in SasView). This model can also be used to model a single helical tape. To do this, set $\epsilon$ = 0. $$I(q) = \frac{\pi}{q L} \sum^{\inf}_{n = 0} \epsilon_{n} \cos^2 \left( \frac{n \epsilon}{2} \right) \frac{\sin^{2} \left( n \omega / 2 \right)}{\left( n \omega / 2 \right)^2} \left[ g_{n} \left( q, R, a \right) \right]^2$$ where $$g_{n} \left( q, R, a \right) = 2 R^{-2} \left(1 - a^{2} \right) \times \int^{R}_{aR} r dr J_{n} \left[ q r \left( 1 - q^{2}_{n}) \right)^{1/2} \right]$$ $$q_{n} = \frac{2 \pi n}{P q}$$ and $L$ is the total length of the tape, $\epsilon$ is the angle of separation between the helices, $\omega$ is the angle of the helical cross section occupied by a tape, $n$ is the order of the layer line, $R$ is the outer radius of the tape, $aR$ is the inner radius of the tape, and $P$ is the helical pitch. References ---------- 1) O. A. Pringle and P. W. Schmidt, Journal of Applied Crystallography, 1971, 4, 290-293, DOI: 10.1107/S002188987100699X 2) C. V. Teixeira, H. Amenitsch, T. Fukushima et al., Journal of Applied Crystallography, 2010, 43, 850-857, DOI: 10.1107/S0021889810015736 The fitting equation can be found in Reference [2] as Equations 15 & 16. Authorship and Verification ---------------------------- * **Author:** Tim Snow **Date:** November 25, 2016 * **Last Modified by:** Tim Snow **Date:** January 23, 2016 * **Last Reviewed by:** Steve King **Date:** November 18, 2022

This is the Pringle-Schmidt equation for fitting the helical form factor of an infinitely long helix formed from two helical tapes wrapped around each other at an angle $\epsilon$. The two helices are assumed to have the same width and thickness. Please see Figure 1 in Reference [1]. Note that this figure uses $\phi$ in place of the $\epsilon$ used here (because $\phi$ has another meaning in SasView).

This model can also be used to model a single helical tape. To do this, set $\epsilon$ = 0.

$$I(q) = \frac{\pi}{q L} \sum^{\inf}_{n = 0} \epsilon_{n} \cos^2 \left( \frac{n \epsilon}{2} \right) \frac{\sin^{2} \left( n \omega / 2 \right)}{\left( n \omega / 2 \right)^2} \left[ g_{n} \left( q, R, a \right) \right]^2$$

where

$$g_{n} \left( q, R, a \right) = 2 R^{-2} \left(1 - a^{2} \right) \times \int^{R}_{aR} r dr J_{n} \left[ q r \left( 1 - q^{2}_{n}) \right)^{1/2} \right]$$

$$q_{n} = \frac{2 \pi n}{P q}$$

and $L$ is the total length of the tape, $\epsilon$ is the angle of separation between the helices, $\omega$ is the angle of the helical cross section occupied by a tape, $n$ is the order of the layer line, $R$ is the outer radius of the tape, $aR$ is the inner radius of the tape, and $P$ is the helical pitch.

References ----------

1) O. A. Pringle and P. W. Schmidt, Journal of Applied Crystallography, 1971, 4, 290-293, DOI: 10.1107/S002188987100699X 2) C. V. Teixeira, H. Amenitsch, T. Fukushima et al., Journal of Applied Crystallography, 2010, 43, 850-857, DOI: 10.1107/S0021889810015736

The fitting equation can be found in Reference [2] as Equations 15 & 16.

Authorship and Verification ----------------------------

* **Author:** Tim Snow **Date:** November 25, 2016 * **Last Modified by:** Tim Snow **Date:** January 23, 2016 * **Last Reviewed by:** Steve King **Date:** November 18, 2022

Source: https://marketplace.sasview.org/models/150/
