import numpy as np
from sklearn.preprocessing import StandardScaler

class TemporalPatternGenerator:
    def __init__(self, num_records, trend_type, trend_value, min_val, max_val):
        self.num_records = num_records
        self.trend_type = trend_type
        self.trend_value = trend_value
        self.min_val = min_val
        self.max_val = max_val

    def generate_temporal_pattern(self):
        time_indices = np.arange(self.num_records)

        if self.trend_type == 'increasing':
            temporal_pattern = (self.trend_value * time_indices) * 100
        elif self.trend_type == 'decreasing':
            temporal_pattern = (-self.trend_value * time_indices) * 100
        elif self.trend_type == 'no_change':
            temporal_pattern = np.zeros(self.num_records)  # No change over time
        else:
            raise ValueError("Invalid trend type. Choose from increasing, decreasing, or no_change.")

        # Scale the temporal pattern using a StandardScaler
        scaler = StandardScaler()
        scaled_temporal_pattern = scaler.fit_transform(temporal_pattern.reshape(-1, 1)).flatten()

        return scaled_temporal_pattern