import numpy as np
from scipy.fftpack import fft
from sklearn.preprocessing import StandardScaler

class SeasonalPatternGenerator:
    def __init__(self, num_records, seasonality_type, min_val, max_val):
        self.num_records = num_records
        self.seasonality_type = seasonality_type
        self.min_val = min_val
        self.max_val = max_val

    def generate_seasonal_pattern(self):
        time_indices = np.arange(self.num_records)

        # Generate a random time series with a seasonal component
        np.random.seed(0)
        signal = np.random.normal(size=self.num_records)

        if self.seasonality_type == 'daily':
            frequency = 24  # Assuming hourly data
        elif self.seasonality_type == 'weekly':
            frequency = 7  # Weekly pattern
        elif self.seasonality_type == 'monthly':
            frequency = 12  # Monthly pattern
        elif self.seasonality_type == 'quarterly':
            frequency = 4  # Quarterly pattern
        elif self.seasonality_type == 'yearly':
            frequency = 1  # Yearly pattern
        else:
            raise ValueError("Invalid seasonality type. Choose from daily, weekly, monthly, quarterly, or yearly.")

        # Add a seasonal component to the signal using Fourier analysis
        fft_signal = fft(signal)
        seasonal_component = np.real(fft_signal[:frequency])
        seasonal_pattern = np.zeros_like(signal)
        for i in range(frequency):
            seasonal_pattern += seasonal_component[i] * np.sin(2 * np.pi * i * time_indices / self.num_records)

        # Scale the seasonal pattern using a StandardScaler
        scaler = StandardScaler()
        scaled_seasonal_pattern = scaler.fit_transform(seasonal_pattern.reshape(-1, 1)).flatten()

        return scaled_seasonal_pattern
