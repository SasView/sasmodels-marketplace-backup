# Casein Micelle Bouchoux

This model comprises three populations of polydisperse hard spheres, corresponding to, from the largest to smallest size: Level0 - The casein micelle, around 100 nm in diameter. Level1 - Hard regions that resist compression and contain the nanoclusters, 10-40 nm in diameter. Level2 - CaP nanoclusters serving as anchors for the casein molecules. The scattering intensity $I(q)$ is the sum of the intensities scattered by the three levels and is calculated as: $I(q) = c \left[ \phi _0 v_0 \left( \Delta p_0 \right) ^2 P_0 \left( q \right) + \phi _1 v_1 \left( \Delta p_1 \right) ^2 P_1 \left( q \right) + \phi _2 v_2 \left( \Delta p_2 \right) ^2 P_2 \left( q \right) \right]$ where $c$ is a constant accounting for the total concentration of the caseins. $\phi _n$ is the volume fraction occupied by the structural element $n$ in the dispersion, while $v_n$ and $\Delta p_n$ are its volume and average scattering contrast, respectively. $P_n \left( q \right)$ are the form factors of each object which are modelled using the expression of Aragon et al. (1976). The form factors are calculated as: $P_n\left(q\right) = \frac{9z!\left(z+1\right)^6}{X^6\left(z+6\right)!}\left[\frac{1}{2}+\frac{1}{2}\left(\frac{z+2}{z+1}\right)X^2+\left[G\left(2X\right)^\left(1/2\right)\left(z+1\right)\times Q \left(X\right)\right]\right]$ where $z = \left(\frac{1}{\sigma}\right)^2 - 1 $ with $\sigma$ being the polydispersity and the functions $G\left(y\right)$ and $Q\left(y\right)$ are: $G\left(y\right) = \frac{\left(z+1\right)^2}{\left(z+1\right)^2 + y^2}$ ; $F\left(y\right) = \arctan\left[y/\left(z + 1\right)\right]$ and $Q\left(X\right) = - \frac{1}{2}\cos\left[\left(z + 1\right)F\left(2X\right)\right] - XG^\frac{1}{2}\left(2X\right)\sin\left[\left(z + 2\right)F\left(2X\right)\right] + \frac{1}{2}X^2\left(\frac{z + 2}{z + 1}\right)G\left(2X\right)\cos\left[\left(z + 3\right)F\left(2X\right)\right] $ References ---------- Bouchoux, A., Gesan-Guiziou, G., Perez, J. and Cabane, B. (2010). How to Squeeze a Sponge: Casein Micelles under Osmotic Stress, a SAXS Study. Biophysical Journal 99, 3754-3762. Aragon, S. R. and R. Pecora. (1976). Theory of dynamic light scattering from polydisperse systems. J. Chem. Phys. 64:2395-2404.

This model comprises three populations of polydisperse hard spheres, corresponding to, from the largest to smallest size: Level0 - The casein micelle, around 100 nm in diameter. Level1 - Hard regions that resist compression and contain the nanoclusters, 10-40 nm in diameter. Level2 - CaP nanoclusters serving as anchors for the casein molecules.

The scattering intensity $I(q)$ is the sum of the intensities scattered by the three levels and is calculated as:

$I(q) = c \left[ \phi _0 v_0 \left( \Delta p_0 \right) ^2 P_0 \left( q \right) + \phi _1 v_1 \left( \Delta p_1 \right) ^2 P_1 \left( q \right) + \phi _2 v_2 \left( \Delta p_2 \right) ^2 P_2 \left( q \right) \right]$

where $c$ is a constant accounting for the total concentration of the caseins. $\phi _n$ is the volume fraction occupied by the structural element $n$ in the dispersion, while $v_n$ and $\Delta p_n$ are its volume and average scattering contrast, respectively. $P_n \left( q \right)$ are the form factors of each object which are modelled using the expression of Aragon et al. (1976).

The form factors are calculated as:

$P_n\left(q\right) = \frac{9z!\left(z+1\right)^6}{X^6\left(z+6\right)!}\left[\frac{1}{2}+\frac{1}{2}\left(\frac{z+2}{z+1}\right)X^2+\left[G\left(2X\right)^\left(1/2\right)\left(z+1\right)\times Q \left(X\right)\right]\right]$

where $z = \left(\frac{1}{\sigma}\right)^2 - 1 $

with $\sigma$ being the polydispersity and the functions $G\left(y\right)$ and $Q\left(y\right)$ are:

$G\left(y\right) = \frac{\left(z+1\right)^2}{\left(z+1\right)^2 + y^2}$ ; $F\left(y\right) = \arctan\left[y/\left(z + 1\right)\right]$

and

$Q\left(X\right) = - \frac{1}{2}\cos\left[\left(z + 1\right)F\left(2X\right)\right] - XG^\frac{1}{2}\left(2X\right)\sin\left[\left(z + 2\right)F\left(2X\right)\right] + \frac{1}{2}X^2\left(\frac{z + 2}{z + 1}\right)G\left(2X\right)\cos\left[\left(z + 3\right)F\left(2X\right)\right] $

References ---------- Bouchoux, A., Gesan-Guiziou, G., Perez, J. and Cabane, B. (2010). How to Squeeze a Sponge: Casein Micelles under Osmotic Stress, a SAXS Study. Biophysical Journal 99, 3754-3762. Aragon, S. R. and R. Pecora. (1976). Theory of dynamic light scattering from polydisperse systems. J. Chem. Phys. 64:2395-2404.

# Example Data:

Source: https://marketplace.sasview.org/models/101/
