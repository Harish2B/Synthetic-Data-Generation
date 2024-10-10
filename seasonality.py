import numpy as np
from sklearn.preprocessing import StandardScaler

class SeasonalPatternGenerator:
    def __init__(self, num_records, seasonality_type, min_val, max_val):
        self.num_records = num_records
        self.seasonality_type = seasonality_type
        self.min_val = min_val
        self.max_val = max_val

    def generate_seasonal_pattern(self):
        time_indices = np.arange(self.num_records)

        if self.seasonality_type == 'daily':
            frequency = 24  # Assuming hourly data
            amplitude = 1  # Adjust amplitude as needed
            seasonal_pattern = amplitude * np.sin(2 * np.pi * frequency * time_indices / self.num_records)
        elif self.seasonality_type == 'weekly':
            frequency = 7  # Weekly pattern
            amplitude = 1
            seasonal_pattern = amplitude * np.sin(2 * np.pi * frequency * time_indices / self.num_records)
        elif self.seasonality_type == 'monthly':
            frequency = 12  # Monthly pattern
            amplitude = 1
            seasonal_pattern = amplitude * np.sin(2 * np.pi * frequency * time_indices / self.num_records)
        elif self.seasonality_type == 'quarterly':
            frequency = 4  # Quarterly pattern
            amplitude = 1
            seasonal_pattern = amplitude * np.sin(2 * np.pi * frequency * time_indices / self.num_records)
        elif self.seasonality_type == 'yearly':
            frequency = 1  # Yearly pattern
            amplitude = 1
            seasonal_pattern = amplitude * np.sin(2 * np.pi * frequency * time_indices / self.num_records)
        else:
            raise ValueError("Invalid seasonality type. Choose from daily, weekly, monthly, quarterly, or yearly.")

        # Scale the seasonal pattern using a StandardScaler
        scaler = StandardScaler()
        scaled_seasonal_pattern = scaler.fit_transform(seasonal_pattern.reshape(-1, 1)).flatten()

        return scaled_seasonal_pattern
