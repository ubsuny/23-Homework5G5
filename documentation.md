# Using the Fourier Transform to Find the Period of Oscillation of CO2 Emission Data

## Introduction

### Fourier Transforms [1]
The Fourier transform is a mathematical method that transforms a function from one variable space to another. Perhaps the most common transformation is from time space to frequency space, i.e. data taken as a function of time can be represented as a function of its frequency of oscillation as well. Analytically, this transformation is given exactly by
$$F(\omega) = \int_{-\infty}^{\infty} e^{-i \omega t} f(t) dt$$
Where $\omega$ is the frequency. However, since computers must rely on numerical methods and cannot perform exact integration, we must use the Discrete Fourier Transform (DFT)
$$F (\omega) = \sum_{k = 0}^{N-1} f(k) e^{\omega k T}$$
Where $T$ is our interval between sampling times.

However, implementing the DFT exactly leads to long computation times for large data sets. To resolve this, we use the Fast Fourier Transform method. Specifically, we use the Cooley-Tukey implementation of the DFT [2], which dramatically speeds up computation time. We start by rewriting our DFT as
$$F (n) = \sum_{k = 0}^{N-1} f(k) e^{- j \frac{2 \pi}{N} n k } = \sum_{k = 0}^{N-1} f(k) W_{N}^{nk}$$
Where
$$W_{N}^{nk} = e^{- j \frac{2 \pi}{N} n k }$$
Where we notice that
$$W_8^4 = -W_8^0$$
$$W_8^5 = -W_8^1$$
And so on, meaning we don't have to repeat this calculation for every single value.

In addition, given an even number of data points, we can divide the imput data into two parts, "even" and "odd" which are computed simultaneously. Combined with the prior principle this will exponentially decrease the computation time.

### Carbon Emissions Monitoring [3]

The Global Monitoring Laboratory (GML) is an organization that uses monitoring stations around the globe to record various sets of environmental data, including carbon dioxide (CO2) emissions. We specifically used the data from the Cape Kumukahi, Hawaii, United States monitoring station [4], along with Fourier transform methods, to measure the frequency of carbon emission cycles.

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

## Calculating Frequency of Data

To find the dominant frequencies of the data, we find the maxima of our frequency spectrum calculated via FFT by first finding the power spectrum of our FFT
``` Python
def fft_power(x):
    N = len(x)
    if N <= 1:
        return x

    power = np.zeros(N // 2 + 1)
    magnitude = np.zeros(N // 2 + 1)

    power[0] = abs(x[0])**2
    magnitude[0] = abs(x[0])

    power[1:N // 2] = abs(x[1:N // 2])**2 + abs(x[N - 1:N // 2:-1])**2
    magnitude[1:N // 2] = abs(x[1:N // 2]) + abs(x[N - 1:N // 2:-1])

    if N % 2 == 0:
        power[N // 2] = abs(x[N // 2])**2
        magnitude[N // 2] = abs(x[N // 2])

    power = power / N
    magnitude = magnitude / N

    return power, magnitude
```
And then checking the maxima of this result using the zeros of the gradient, giving our peak frequencies of the data
``` Python

def find_fft_peaks_derivative_with_gradient(freq_values, power_spectrum, threshold=0.5):
    # Compute the gradient of the power spectrum
    gradient = np.gradient(power_spectrum)

    # Find indices where the gradient changes sign from positive to negative
    peak_indices = np.where((gradient[:-1] > 0) & (gradient[1:] < 0))[0] + 1

    # Filter peaks based on threshold
    peak_indices = peak_indices[power_spectrum[peak_indices] > threshold]

    # Extract corresponding frequencies
    peak_freqs = freq_values[peak_indices]

    return peak_freqs
```

## <ins>References:</ins>
1. [Discrete Fourier Transforms](https://www.robots.ox.ac.uk/~sjrob/Teaching/SP/l7.pdf)
2. [Cooley-Tukey Method (Lecture Notes)](https://cdn.discordapp.com/attachments/1145841446180630628/1169348831746474096/2023-410-11-fft.pdf?ex=655e4e76&is=654bd976&hm=a2547cbdee88128abd43e6b1e884a13fe8eec49716d273097d57e7581ba3d3b6&)
3. [Global Monitoring Laboratory](https://gml.noaa.gov/)
4. [Cape Kumukahi, Hawaii, United States GML Data](https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_kum_surface-flask_1_ccgg_month.txt.)
