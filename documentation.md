# Using the Fourier Transform to Find the Period of Oscillation of CO2 Emission Data

## Introduction

### Fourier Transforms [https://phys.libretexts.org/Learning_Objects/Demos_Techniques_and_Experiments/Fourier_Transform_A_Brief_Introduction]
The Fourier transform is a mathematical method that transforms a function from one variable space to another. Perhaps the most common transformation is from time space to frequency space, i.e. data taken as a function of time can be represented as a function of its frequency of oscillation as well. Analytically, this transformation is given exactly by
$$F(\omega) = \int_{-\infty}^{\infty} e^{-i \omega t} f(t) dt$$
Where $\omega$ is the frequency. However, since computers must rely on numerical methods and cannot perform exact integration, we must use the Discrete Fourier Transform (DFT) [https://www.robots.ox.ac.uk/~sjrob/Teaching/SP/l7.pdf]
$$F (\omega) = \sum_{k = 0}^{N-1} f(k) e^{\omega k T}$$
Where $T$ is our interval between sampling times.

However, implementing the DFT exactly leads to long computation times for large data sets. To resolve this, we use the Fast Fourier Transform method. Specifically, we use the Cooley-Tukey implementation of the DFT, which dramatically speeds up computation time. We start by rewriting our DFT as
$$F (n) = \sum_{k = 0}^{N-1} f(k) e^{- j \frac{2 \pi}{N} n k } = \sum_{k = 0}^{N-1} f(k) W_{N}^{nk}$$
Where
$$W_{N}^{nk} = e^{- j \frac{2 \pi}{N} n k }$$
Where we notice that
$$W_8^4 = -W_8^0$$
$$W_8^5 = -W_8^1$$
And so on, meaning we don't have to repeat this calculation for every single value.

In addition, given an even number of data points, we can divide the imput data into two parts, "even" and "odd" which are computed simultaneously. Combined with the prior principle this will exponentially decrease the computation time.

### Carbon Emissions Monitoring [https://gml.noaa.gov/]

The Global Monitoring Laboratory (GML) is an organization that uses monitoring stations around the globe to record various sets of environmental data, including carbon dioxide (CO2) emissions. We specifically used the data from the Cape Kumukahi, Hawaii, United States monitoring station, along with Fourier transform methods, to measure the frequency of carbon emission cycles. The data used is available here: https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_kum_surface-flask_1_ccgg_month.txt.

## Coding the FFT

Our program contains functions to perform both the DFT and FFT for a given data set. The DFT is relatively straightforward, taking an input data array and "brute forcing" the above DFT summation
``` Python
def discrete_transform(data):
    N = len(data)
    transform = np.zeros(N)
    for k in range(N):
        for j in range(N):
            angle = 2 * pi * k * j / N
            transform[k] += data[j] * exp(1j * angle)
    return transform
```

For the FFT, the process is slightly more complex. First, we check to ensure that we have an even number of data points, and that we actually have more than one data point at all, which are both required to use our algorithm explained above. If we do not, we simply perform the discrete transform as usual.
``` Python
if N <= 1: return x
    elif N % 2 == 1:         # N is odd, lemma does not apply
        print ('N is ' + str(N) + ', fall back to discrete transform')
        return discrete_transform(x)
```

For an even number of data points, we then split the data into two parts and perform the calculation above
``` Python
even = fft(x[0::2])
    odd =  fft(x[1::2])
    return np.array( [even[k] + exp(-2j*pi*k/N)*odd[k] for k in range(N//2)] + \
                     [even[k] - exp(-2j*pi*k/N)*odd[k] for k in range(N//2)] )
```
Which will give the DFT in less time.

## Calculating Power Spectrum
