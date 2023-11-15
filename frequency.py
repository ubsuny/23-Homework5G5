# This script calculates the FFT of monthly averaged CO2 data and determines the peak frequency.

import numpy as np
import pandas as pd

# Data Source: Arembepe, Bahia, Brazil (ABP)
# Data Link: https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_abp_surface-flask_1_ccgg_month.txt

def calculate_peak_frequency(data_file):
    try:
        # Load the data from the file
        data = pd.read_csv(data_file, delimiter=',', header=0)

        # Extract the CO2 values
        co2_methane_data = data['value']

        # Calculate the FFT
        fft_result = np.fft.fft(co2_methane_data)

        # Calculate the frequency of the peak(s) considering the sampling interval
        sampling_interval_seconds = 2629440  # Approximate sampling interval for one month in seconds
        data_length = len(co2_methane_data)
        sampling_rate = 1 / sampling_interval_seconds  # Effective sampling rate in Hz

        # Find the indices with the highest amplitude
        peak_indices = np.argmax(np.abs(fft_result))

        # Calculate the frequency in Hz
        frequency_hz = peak_indices * (sampling_rate / data_length)

        return frequency_hz
    except FileNotFoundError:
        print("Data file not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

data_file = 'data_file.csv'
peak_frequency = calculate_peak_frequency(data_file)

if peak_frequency is not None:
    print(f"The frequency of the peak is approximately {peak_frequency} Hz.")
