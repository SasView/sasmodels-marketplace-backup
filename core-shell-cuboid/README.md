# Core shell cuboid

Output: P(q) = \frac{\text{scale}}{V_{cs}} \int_{0}^{\pi}\int_{0}^{2\pi} f^2(q,\theta_Q,\phi_Q) \sin(\theta_Q) d\theta_Q d\phi_Q + \text{background} where f(q,\theta_Q,\phi_Q) = ( \rho_{c}-\rho_{sh} ) \prod_{j=1}^3 [ 2 * L/2 * sinc(Q_j*L/2) ] + ( \rho_{sh}-\rho_{solv} ) * \prod_{j=1}^3 [ 2 * (L/2+d) * sinc(Q_j*(L/2+d)) ] where sinc(x) = \sin(x) / x Q_1 = Q \sin(\theta_Q) \cos(\phi_Q) Q_2 = Q \sin(\theta_Q) \sin(\phi_Q) Q_3 = Q \cos(\theta_Q) Parameters: scale = scaling factor, volume fraction of particles scale phi ~ N V_{cs} / V_{irr}, with N / V_{irr} being the number density of particles in the irradiated volume background = const. background L = length of the cuboid d = shell thickness \rho_{c} = scattering length density of core \rho_{sh} = scattering length density of shell \rho_{solv} = scattering length density of solvent V_{cs} = volume of core-shell cuboid Intensity is very similar to the faster core-shell sphere model, especially when using polydispersity. Model can easily be generalized for anisotropic lengths.

Output: P(q) = \frac{\text{scale}}{V_{cs}} \int_{0}^{\pi}\int_{0}^{2\pi} f^2(q,\theta_Q,\phi_Q) \sin(\theta_Q) d\theta_Q d\phi_Q + \text{background}

where f(q,\theta_Q,\phi_Q) = ( \rho_{c}-\rho_{sh} ) \prod_{j=1}^3 [ 2 * L/2 * sinc(Q_j*L/2) ] + ( \rho_{sh}-\rho_{solv} ) * \prod_{j=1}^3 [ 2 * (L/2+d) * sinc(Q_j*(L/2+d)) ]

where sinc(x) = \sin(x) / x

Q_1 = Q \sin(\theta_Q) \cos(\phi_Q) Q_2 = Q \sin(\theta_Q) \sin(\phi_Q) Q_3 = Q \cos(\theta_Q)

Parameters: scale = scaling factor, volume fraction of particles scale phi ~ N V_{cs} / V_{irr}, with N / V_{irr} being the number density of particles in the irradiated volume background = const. background L = length of the cuboid d = shell thickness \rho_{c} = scattering length density of core \rho_{sh} = scattering length density of shell \rho_{solv} = scattering length density of solvent V_{cs} = volume of core-shell cuboid

Intensity is very similar to the faster core-shell sphere model, especially when using polydispersity. Model can easily be generalized for anisotropic lengths.

Source: https://marketplace.sasview.org/models/114/
