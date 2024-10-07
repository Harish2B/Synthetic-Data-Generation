"""
In this module, for the synthetic data we have created to be more realistic, we are adding noise and outliers to make it more realistic.
we are adding 3 main function as user input.
noise level- it creates the noise percentage of how much the user needs as percentage (optimal value is between 0-0.1)
outlier proportion- it gets the number of outliers needs to be created as percentage. (optimal value is between 0-0.1)
outlier magnitude- it gets the value of how far these outliers needs to be placed (optimal value is between 1-3)
"""

import numpy as np

class DataNoiser:
    def __init__(self, data):
        self.data = data

    def add_noise(self, noise_level):
        self.data += np.random.normal(0, noise_level, size=self.data.shape)

    def add_outliers(self, outlier_proportion, outlier_magnitude):
        num_outliers = int(outlier_proportion * len(self.data))
        outlier_indices = np.random.choice(self.data.index, size=num_outliers, replace=False)

        for col in self.data.columns:
            self.data.loc[outlier_indices, col] += np.random.uniform(-outlier_magnitude, outlier_magnitude, size=num_outliers)
