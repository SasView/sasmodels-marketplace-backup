# Stacked Disks

Definition This model provides the form factor, $P(q)$, for stacked discs (tactoids) with a core/layer structure which is constructed itself as $P(q) S(Q)$ multiplying a $P(q)$ for individual core/layer disks by a structure factor $S(q)$ proposed by Kratky and Porod in 1949[#Kratky1949]_ assuming the next neighbor distance (d-spacing) in the stack of parallel discs obeys a Gaussian distribution. As such the normalization of this "composite" form factor is relative to the individual disk volume, not the volume of the stack of disks. This model is appropriate for example for non non exfoliated clay particles such as Laponite. Geometry of a single core/layer disk The scattered intensity $I(q)$ is calculated as $$  I(q) = N\int_{0}^{\pi /2}\left[ \Delta \rho_t \left( V_t f_t(q,\alpha) - V_c f_c(q,\alpha)\right) + \Delta \rho_c V_c f_c(q,\alpha)\right]^2 S(q,\alpha)\sin{\alpha}\ d\alpha + \text{background} $$ where the contrast $$  \Delta \rho_i = \rho_i - \rho_\text{solvent} $$ and $N$ is the number of individual (single) discs per unit volume, $\alpha$ is the angle between the axis of the disc and $q$, and $V_t$ and $V_c$ are the total volume and the core volume of a single disc, respectively, and $$  f_t(q,\alpha) = \left(\frac{\sin(q(d+h)\cos{\alpha})}{q(d+h)\cos{\alpha}}\right) \left(\frac{2J_1(qR\sin{\alpha})}{qR\sin{\alpha}} \right) $$ f_c(q,\alpha) =     \left(\frac{\sin(qh)\cos{\alpha})}{qh\cos{\alpha}}\right)     \left(\frac{2J_1(qR\sin{\alpha})}{qR\sin{\alpha}}\right) where $d$ = thickness of the layer (*thick_layer*), $2h$ = core thickness (*thick_core*), and $R$ = radius of the disc (*radius*). $$  S(q,\alpha) = 1 + \frac{1}{2}\sum_{k=1}^n(n-k)\cos{(kDq\cos{\alpha})} \exp\left[ -k(q)^2(D\cos{\alpha}~\sigma_d)^2/2\right] $$ where $n$ is the total number of the disc stacked (*n_stacking*), $D = 2(d+h)$ is the next neighbor center-to-center distance (d-spacing), and $\sigma_d$ = the Gaussian standard deviation of the d-spacing (*sigma_d*). Note that $D\cos(\alpha)$ is the component of $D$ parallel to $q$ and the last term in the equation above is effectively a Debye-Waller factor term. .. note:: 1. Each assembly in the stack is layer/core/layer, so the spacing of the     cores is core plus two layers. The 2nd virial coefficient of the cylinder     is calculated based on the *radius* and *length*     = *n_stacking* * (*thick_core* + 2 * *thick_layer*)     values, and used as the effective radius for $S(Q)$ when $P(Q) * S(Q)$     is applied. 2. the resolution smearing calculation uses 76 Gaussian quadrature points     to properly smear the model since the function is HIGHLY oscillatory,     especially around the q-values that correspond to the repeat distance of     the layers. 2d scattering from oriented stacks is calculated in the same way as for cylinders, for further details of the calculation and angular dispersions see `orientation`. Angles $\theta$ and $\phi$ orient the stack of discs relative     to the beam line coordinates, where the beam is along the $z$ axis.     Rotation $\theta$, initially in the $xz$ plane, is carried out first,     then rotation $\phi$ about the $z$ axis. Orientation distributions are     described as rotations about two perpendicular axes $\delta_1$ and     $\delta_2$ in the frame of the cylinder itself, which when     $\theta = \phi = 0$ are parallel to the $Y$ and $X$ axes. Our model is derived from the form factor calculations implemented in a C-library provided by the NIST Center for Neutron Research[#Kline2006]_ References See also Higgins and Benoit [#Higgins1994]_ and Guinier and Fournet [#Guinier1955]_. .. [#Kratky1949] O Kratky and G Porod, *J. Colloid Science*, 4, (1949) 35 .. [#Kline2006] S R Kline, *J Appl. Cryst.*, 39 (2006) 895 .. [#Higgins1994] J S Higgins and H C Benoit, *Polymers and Neutron Scattering*,    Clarendon, Oxford, 1994 .. [#Guinier1955] A Guinier and G Fournet, *Small-Angle Scattering of X-Rays*,    John Wiley and Sons, New York, 1955 Authorship and Verification **Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Paul Butler and Paul Kienzle **Date:** November 26, 2016 **Last Reviewed by:** Paul Butler and Paul Kienzle **Date:** November 26, 2016

Definition

This model provides the form factor, $P(q)$, for stacked discs (tactoids) with a core/layer structure which is constructed itself as $P(q) S(Q)$ multiplying a $P(q)$ for individual core/layer disks by a structure factor $S(q)$ proposed by Kratky and Porod in 1949[#Kratky1949]_ assuming the next neighbor distance (d-spacing) in the stack of parallel discs obeys a Gaussian distribution. As such the normalization of this "composite" form factor is relative to the individual disk volume, not the volume of the stack of disks. This model is appropriate for example for non non exfoliated clay particles such as Laponite.

Geometry of a single core/layer disk

The scattered intensity $I(q)$ is calculated as

$$  I(q) = N\int_{0}^{\pi /2}\left[ \Delta \rho_t \left( V_t f_t(q,\alpha) - V_c f_c(q,\alpha)\right) + \Delta \rho_c V_c f_c(q,\alpha)\right]^2 S(q,\alpha)\sin{\alpha}\ d\alpha + \text{background} $$ where the contrast

$$  \Delta \rho_i = \rho_i - \rho_\text{solvent} $$ and $N$ is the number of individual (single) discs per unit volume, $\alpha$ is the angle between the axis of the disc and $q$, and $V_t$ and $V_c$ are the total volume and the core volume of a single disc, respectively, and

$$  f_t(q,\alpha) = \left(\frac{\sin(q(d+h)\cos{\alpha})}{q(d+h)\cos{\alpha}}\right) \left(\frac{2J_1(qR\sin{\alpha})}{qR\sin{\alpha}} \right) $$ f_c(q,\alpha) =     \left(\frac{\sin(qh)\cos{\alpha})}{qh\cos{\alpha}}\right)     \left(\frac{2J_1(qR\sin{\alpha})}{qR\sin{\alpha}}\right)

where $d$ = thickness of the layer (*thick_layer*), $2h$ = core thickness (*thick_core*), and $R$ = radius of the disc (*radius*).

$$  S(q,\alpha) = 1 + \frac{1}{2}\sum_{k=1}^n(n-k)\cos{(kDq\cos{\alpha})} \exp\left[ -k(q)^2(D\cos{\alpha}~\sigma_d)^2/2\right] $$ where $n$ is the total number of the disc stacked (*n_stacking*), $D = 2(d+h)$ is the next neighbor center-to-center distance (d-spacing), and $\sigma_d$ = the Gaussian standard deviation of the d-spacing (*sigma_d*). Note that $D\cos(\alpha)$ is the component of $D$ parallel to $q$ and the last term in the equation above is effectively a Debye-Waller factor term.

.. note::

1. Each assembly in the stack is layer/core/layer, so the spacing of the     cores is core plus two layers. The 2nd virial coefficient of the cylinder     is calculated based on the *radius* and *length*     = *n_stacking* * (*thick_core* + 2 * *thick_layer*)     values, and used as the effective radius for $S(Q)$ when $P(Q) * S(Q)$     is applied.

2. the resolution smearing calculation uses 76 Gaussian quadrature points     to properly smear the model since the function is HIGHLY oscillatory,     especially around the q-values that correspond to the repeat distance of     the layers.

2d scattering from oriented stacks is calculated in the same way as for cylinders, for further details of the calculation and angular dispersions see `orientation`.

Angles $\theta$ and $\phi$ orient the stack of discs relative     to the beam line coordinates, where the beam is along the $z$ axis.     Rotation $\theta$, initially in the $xz$ plane, is carried out first,     then rotation $\phi$ about the $z$ axis. Orientation distributions are     described as rotations about two perpendicular axes $\delta_1$ and     $\delta_2$ in the frame of the cylinder itself, which when     $\theta = \phi = 0$ are parallel to the $Y$ and $X$ axes.

Our model is derived from the form factor calculations implemented in a C-library provided by the NIST Center for Neutron Research[#Kline2006]_

References

See also Higgins and Benoit [#Higgins1994]_ and Guinier and Fournet [#Guinier1955]_.

.. [#Kratky1949] O Kratky and G Porod, *J. Colloid Science*, 4, (1949) 35 .. [#Kline2006] S R Kline, *J Appl. Cryst.*, 39 (2006) 895 .. [#Higgins1994] J S Higgins and H C Benoit, *Polymers and Neutron Scattering*,    Clarendon, Oxford, 1994 .. [#Guinier1955] A Guinier and G Fournet, *Small-Angle Scattering of X-Rays*,    John Wiley and Sons, New York, 1955

Authorship and Verification

**Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Paul Butler and Paul Kienzle **Date:** November 26, 2016 **Last Reviewed by:** Paul Butler and Paul Kienzle **Date:** November 26, 2016

Source: https://marketplace.sasview.org/models/32/
