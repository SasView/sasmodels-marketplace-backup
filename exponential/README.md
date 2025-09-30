# Exponential

Flexible exponential model with a flat background. DEFINITION This model calculates a variety of exponential functions. The scattered intensity $I(q)$ is calculated as $I(q) = \text{scale} \cdot exp(-\text{prefactor} \cdot q^{\text{exponent}}) + \text{background}$ Note the minus sign in the exponential term. Thus if $prefactor$ is entered as a positive number during fitting the returned function will decrease as $q$ increases. Also note that unlike many other models, $scale$ in this model is NOT explicitly related to a volume fraction. Be careful if combining this model with other models. The value of $exponent$ controls the behaviour of the function. When: $exponent$=1     : a normal exponential function is returned 0<$exponent$<1 : a so-called stretched exponential (or Kohlrausch-Williams-Watts, KWW) [1,2] function is returned $exponent$>1     : a compressed exponential is returned $exponent$=2     : a normal distribution function is returned. This model probably has limited applicability in the analysis of SAS data but is of great use in allied fields. For example, the KWW function is used in the analysis of dielectric spectra data, rheological relaxation data, and dynamic light scattering (photon correlation spectroscopy) data. REFERENCES 1.  R. Kohlrausch, Annalen der Physik und Chemie, 91(1) (1854) 56-82 & 179-213 2.  G. Williams & D.C. Watts,Transactions of the Faraday Society, 66 (1970) 80-85

Flexible exponential model with a flat background.

DEFINITION This model calculates a variety of exponential functions.

The scattered intensity $I(q)$ is calculated as

$I(q) = \text{scale} \cdot exp(-\text{prefactor} \cdot q^{\text{exponent}}) + \text{background}$

Note the minus sign in the exponential term. Thus if $prefactor$ is entered as a positive number during fitting the returned function will decrease as $q$ increases.

Also note that unlike many other models, $scale$ in this model is NOT explicitly related to a volume fraction. Be careful if combining this model with other models.

The value of $exponent$ controls the behaviour of the function. When:

$exponent$=1     : a normal exponential function is returned

0<$exponent$<1 : a so-called stretched exponential (or Kohlrausch-Williams-Watts, KWW) [1,2] function is returned

$exponent$>1     : a compressed exponential is returned

$exponent$=2     : a normal distribution function is returned.

This model probably has limited applicability in the analysis of SAS data but is of great use in allied fields. For example, the KWW function is used in the analysis of dielectric spectra data, rheological relaxation data, and dynamic light scattering (photon correlation spectroscopy) data.

REFERENCES 1.  R. Kohlrausch, Annalen der Physik und Chemie, 91(1) (1854) 56-82 & 179-213 2.  G. Williams & D.C. Watts,Transactions of the Faraday Society, 66 (1970) 80-85

Source: https://marketplace.sasview.org/models/123/
