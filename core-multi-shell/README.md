# Core Multi Shell

Definition This model is a trivial extension of the CoreShell function to a larger number of shells. The scattering length density profile for the default sld values (w/ 4 shells). SLD profile of the core_multi_shell object from the center of sphere out     for the default SLDs.* The 2D scattering intensity is the same as $P(q)$ above, regardless of the orientation of the $\vec q$ vector which is defined as $$  q = \sqrt{q_x^2 + q_y^2} $$ .. note:: **Be careful!** The SLDs and scale can be highly correlated. Hold as          many of these parameters fixed as possible. .. note:: The outer most radius (= *radius* + *thickness*) is used as the           effective radius for $S(Q)$ when $P(Q)*S(Q)$ is applied. For information about polarised and magnetic scattering, see the `magnetism` documentation. Our model uses the form factor calculations implemented in a C-library provided by the NIST Center for Neutron Research [#Kline2006]_. References Also see the `core-shell-sphere` model documentation and [#Feigin1987]_ .. [#Kline2006] S R Kline, *J Appl. Cryst.*, 39 (2006) 895 .. [#Feigin1987] L A Feigin and D I Svergun, *Structure Analysis by    Small-Angle X-Ray and Neutron Scattering*, Plenum Press, New York, 1987. Authorship and Verification **Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Paul Kienzle **Date:** September 12, 2016 **Last Reviewed by:** Paul Kienzle **Date:** September 12, 2016

Definition

This model is a trivial extension of the CoreShell function to a larger number of shells. The scattering length density profile for the default sld values (w/ 4 shells).

SLD profile of the core_multi_shell object from the center of sphere out     for the default SLDs.*

The 2D scattering intensity is the same as $P(q)$ above, regardless of the orientation of the $\vec q$ vector which is defined as

$$  q = \sqrt{q_x^2 + q_y^2} $$ .. note:: **Be careful!** The SLDs and scale can be highly correlated. Hold as          many of these parameters fixed as possible.

.. note:: The outer most radius (= *radius* + *thickness*) is used as the           effective radius for $S(Q)$ when $P(Q)*S(Q)$ is applied.

For information about polarised and magnetic scattering, see the `magnetism` documentation.

Our model uses the form factor calculations implemented in a C-library provided by the NIST Center for Neutron Research [#Kline2006]_.

References

Also see the `core-shell-sphere` model documentation and [#Feigin1987]_

.. [#Kline2006] S R Kline, *J Appl. Cryst.*, 39 (2006) 895

.. [#Feigin1987] L A Feigin and D I Svergun, *Structure Analysis by    Small-Angle X-Ray and Neutron Scattering*, Plenum Press, New York, 1987.

Authorship and Verification

**Author:** NIST IGOR/DANSE **Date:** pre 2010 **Last Modified by:** Paul Kienzle **Date:** September 12, 2016 **Last Reviewed by:** Paul Kienzle **Date:** September 12, 2016

Source: https://marketplace.sasview.org/models/19/
