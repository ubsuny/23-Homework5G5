# Using the Fourier Transform to Find the Period of Oscillation of CO2 Emission Data

## Introduction

### Fourier Transforms [https://phys.libretexts.org/Learning_Objects/Demos_Techniques_and_Experiments/Fourier_Transform_A_Brief_Introduction]
The Fourier transform is a mathematical method that transforms a function from one variable space to another. Perhaps the most common transformation is from time space to frequency space, i.e. data taken as a function of time can be represented as a function of its frequency of oscillation as well. Analytically, this transformation is given exactly by
$$F(\omega) = \int_{-\infty}^{\infty} e^{-i \omega t} f(t) dt$$
Where $\omega$ is the frequency. However, since computers must rely on numerical methods and cannot perform exact integration, we must use the Discrete Fourier Transform (DFT) [https://www.robots.ox.ac.uk/~sjrob/Teaching/SP/l7.pdf]
$$F (\omega) = \sum_{k = 0}^{N-1} f(k) e^{\omega k T}$$
Where $T$ is our interval between sampling times.

However, implementing the DFT exactly leads to long computation times for large data sets. To resolve this, we use the **Whatever method**
