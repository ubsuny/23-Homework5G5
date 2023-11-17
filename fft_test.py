import pytest
from cmath import exp, pi
from math import sin, cos
import numpy as np

from fft import discrete_transform, fft, fft_power

@pytest.mark.parametrize("input_data, expected_transform", [
    (np.array([sin(2 * pi * x) for x in range(10)]), np.fft.fft(np.array([sin(2 * pi * x) for x in range(10)]))),
    (np.array([1, 2, 3, 4]), np.fft.fft(np.array([1, 2, 3, 4]))),
    (np.array([1, 2, 3, 4, 5]), np.fft.fft(np.array([1, 2, 3, 4, 5]))),
    (np.array([1, 2, 3, 4, 5, 6]), np.fft.fft(np.array([1, 2, 3, 4, 5, 6]))),
])
def test_discrete_transform(input_data, expected_transform):
    transform = discrete_transform(input_data)
    assert np.allclose(transform, expected_transform)

def test_fft_small_input():
    data = np.array([1, 2, 3, 4])
    transform = fft(data)
    expected_transform = np.fft.fft(data)
    assert np.allclose(transform, expected_transform)

def test_fft_odd_input():
    data = np.array([1, 2, 3, 4, 5])
    transform = fft(data)
    expected_transform = np.fft.fft(data)
    assert np.allclose(transform, expected_transform)

def test_fft_even_input():
    data = np.array([1, 2, 3, 4, 5, 6])
    transform = fft(data)
    expected_transform = np.fft.fft(data)
    assert np.allclose(transform, expected_transform)

def test_fft_power():
    data = np.array([sin(2 * pi * x) for x in range(10)])
    power, magnitude = fft_power(data)
    expected_power = np.abs(np.fft.fft(data)) ** 2
    expected_magnitude = np.abs(np.fft.fft(data))
    assert np.allclose(power, expected_power)
    assert np.allclose(magnitude, expected_magnitude)
