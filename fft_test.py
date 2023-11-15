import unittest
from cmath import exp, pi
from math import sin, cos
import numpy as np

from fourier import discrete_transform, fft, fft_power

class FourierTest(unittest.TestCase):

    def test_discrete_transform(self):
        # Test with a simple sine wave
        data = np.array([sin(2 * pi * x) for x in range(10)])
        transform = discrete_transform(data)
        expected_transform = np.fft.fft(data)
        self.assertTrue(np.allclose(transform, expected_transform))

    def test_fft_small_input(self):
        # Test with a small input array
        data = np.array([1, 2, 3, 4])
        transform = fft(data)
        expected_transform = np.fft.fft(data)
        self.assertTrue(np.allclose(transform, expected_transform))

    def test_fft_odd_input(self):
        # Test with an odd-length input array
        data = np.array([1, 2, 3, 4, 5])
        transform = fft(data)
        expected_transform = np.fft.fft(data)
        self.assertTrue(np.allclose(transform, expected_transform))

    def test_fft_even_input(self):
        # Test with an even-length input array
        data = np.array([1, 2, 3, 4, 5, 6])
        transform = fft(data)
        expected_transform = np.fft.fft(data)
        self.assertTrue(np.allclose(transform, expected_transform))

    def test_fft_power(self):
        # Test with a simple sine wave
        data = np.array([sin(2 * pi * x) for x in range(10)])
        power, magnitude = fft_power(data)
        expected_power = np.abs(np.fft.fft(data))**2
        expected_magnitude = np.abs(np.fft.fft(data))
        self.assertTrue(np.allclose(power, expected_power))
        self.assertTrue(np.allclose(magnitude, expected_magnitude))

if __name__ == '__main__':
    unittest.main()
