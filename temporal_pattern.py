import numpy as np
from sklearn.preprocessing import MinMaxScaler


class TemporalPatternGenerator:
    def __init__(self, num_records: int, trend_type: str, trend_value: float, min_val: float, max_val: float):
        self.num_records = num_records
        self.trend_type = trend_type
        self.trend_value = trend_value
        self.min_val = min_val
        self.max_val = max_val

    def generate_temporal_pattern(self) -> np.ndarray:
        time_indices = np.arange(self.num_records)

        # Generate the temporal pattern based on the trend type
        if self.trend_type == 'increasing':
            temporal_pattern = self.trend_value * time_indices / (self.num_records - 1)  # Normalize to [0, trend_value]
        elif self.trend_type == 'decreasing':
            temporal_pattern = self.trend_value * (1 - time_indices / (self.num_records - 1))  # Normalize to [trend_value, 0]
        elif self.trend_type == 'no change':
            temporal_pattern = np.zeros(self.num_records)  # No change over time
        else:
            raise ValueError("Invalid trend type. Choose from increasing, decreasing, or no change.")

        # Scale the temporal pattern to the specified range [min_val, max_val]
        scaler = MinMaxScaler()
        scaled_temporal_pattern = scaler.fit_transform(temporal_pattern.reshape(-1, 1)).flatten()

        return scaled_temporal_pattern
