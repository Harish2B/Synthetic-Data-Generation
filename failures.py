import numpy as np
import pandas as pd
import random
from seasonality import SeasonalPatternGenerator

def generate_gaussian_pattern(length: int, peak_value: float) -> np.ndarray:
    """Generate a Gaussian rise and fall pattern."""
    x = np.linspace(-2, 2, length)  # Create a range of x values
    gaussian = np.exp(-x**2)  # Gaussian function
    gaussian = gaussian / gaussian.max() * peak_value  # Scale to peak_value
    return gaussian

def generate_random_seasonal_failures(dataframe: pd.DataFrame, failure_percentage: float, min_peak_value: float, max_peak_value: float, seasonality_type: str) -> pd.DataFrame:
    total_entries = len(dataframe)
    num_failures = int(total_entries * (failure_percentage / 100))

    # Ensure num_failures does not exceed total_entries
    num_failures = min(num_failures, total_entries)

    # Create a copy of the original data to modify
    modified_dataframe = dataframe.copy()

    # Generate seasonal pattern
    seasonal_generator = SeasonalPatternGenerator(total_entries, seasonality_type, min_peak_value, max_peak_value)
    seasonal_pattern = seasonal_generator.generate_seasonal_pattern()

    for _ in range(num_failures):
        # Randomly select a starting index for the seasonal failure
        start_index = random.randint(0, total_entries - 1)

        # Randomly determine the maximum length of the seasonal failure
        max_length = min(50, total_entries - start_index)  # Ensure we don't exceed the bounds
        length = random.randint(30, max_length)

        # Randomly choose whether to create a peak or a drop
        is_peak = random.choice([True, False])

        # Generate a peak value based on whether it's a peak or drop
        if is_peak:
            peak_value = np.random.uniform(min_peak_value, max_peak_value)  # For peaks
            gaussian_pattern = generate_gaussian_pattern(length, peak_value)
        else:
            peak_value = np.random.uniform(min_peak_value, max_peak_value)  # For drops (positive values)
            gaussian_pattern = generate_gaussian_pattern(length, -peak_value)  # Invert for drop

        # Apply the seasonal failure to the selected range
        for i in range(length):
            if start_index + i < total_entries:  # Ensure we don't go out of bounds
                new_value = modified_dataframe.iloc[start_index + i] + seasonal_pattern[start_index + i] + gaussian_pattern[i]

                # Ensure the new value is within the specified limits
                new_value = np.clip(new_value, modified_dataframe.iloc[start_index + i] + min_peak_value, modified_dataframe.iloc[start_index + i] + max_peak_value)

                # Update the modified dataframe
                modified_dataframe.iloc[start_index + i] = new_value

    # Generate random indices for anomalies
    anomaly_indices = random.sample(range(total_entries), num_failures)

    # Generate random anomaly values within the specified range
    anomaly_values = np.random.uniform(min_peak_value, max_peak_value, num_failures)

    for i, index in enumerate(anomaly_indices):
        # Randomly decide whether to add or subtract the anomaly value
        if random.choice([True, False]):
            new_value = modified_dataframe.iloc[index] + anomaly_values[i]  # Peak
        else:
            new_value = modified_dataframe.iloc[index] - anomaly_values[i]  # Drop

        # Ensure the new value is within the specified limits
        new_value = np.clip(new_value, modified_dataframe.iloc[index] + min_peak_value, modified_dataframe.iloc[index] + max_peak_value)

        # Update the modified dataframe
        modified_dataframe.iloc[index] = new_value

    return modified_dataframe
