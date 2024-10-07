"""In this module, we are creating a few relationships for the attributes.
the user inputs what relationship they hold and whether if they are independent or dependent attribute.
with these information, the formula below are substituted and the synthetic data is generated."""

import random
import numpy as np

class apply_relationship:
    def __init__(self, data, relationships, constraints):
        self.data = data
        self.relationships = relationships
        self.constraints = constraints

    def apply_relationships(self):

        for relationship in self.relationships:
            dependent_attrib = relationship['dependent']
            independent_attrib = relationship['independent'][0]  # assuming only one independent attribute
            min_val, max_val = self.constraints[dependent_attrib]['min'], self.constraints[dependent_attrib]['max']
            independent_min_val, independent_max_val = self.constraints[independent_attrib]['min'], self.constraints[independent_attrib]['max']

            dependent_values = []  # Define dependent_values here

            if relationship['type'] == 'linear':
                slope = random.uniform(-0.5, 0.5)  # limit the slope to a reasonable range
                intercept = random.uniform(-1, 1)  # limit the intercept to a reasonable range
                dependent_values = [slope * x + intercept for x in self.data[independent_attrib]]
            elif relationship['type'] == 'parabolic':
                a = random.uniform(-0.5, 0.5)  # limit the coefficient to a reasonable range
                h = random.uniform(-5, 5)  # limit the horizontal shift to a reasonable range
                k = random.uniform(-5, 5)  # limit the vertical shift to a reasonable range
                dependent_values = [a * (x - h) ** 2 + k for x in self.data[independent_attrib]]
            elif relationship['type'] == 'exponential':
                a = random.uniform(0.5, 2)  # limit the coefficient to a reasonable range
                b = random.uniform(-1, 1)  # limit the exponent to a reasonable range
                dependent_values = [a * np.exp(b * x) for x in self.data[independent_attrib]]
            elif relationship['type'] == 'sinusoidal':
                a = random.uniform(-1, 1)  # limit the amplitude to a reasonable range
                b = random.uniform(-1, 1)  # limit the frequency to a reasonable range
                dependent_values = [a * np.sin(b * x) for x in self.data[independent_attrib]]
            elif relationship['type'] == 'hyperbolic':
                a = random.uniform(-1, 1)  # limit the coefficient to a reasonable range
                b = random.uniform(-1, 1)  # limit the exponent to a reasonable range
                dependent_values = [a * (1 / (1 + b * x)) for x in self.data[independent_attrib]]
            elif relationship['type'] == 'sigmoid':
                a = random.uniform(0.5, 2)  # limit the coefficient to a reasonable range
                b = random.uniform(-0.5, 5)  # limit the shift to a reasonable range
                dependent_values = [1 / (1 + np.exp(-a * x + b)) for x in self.data[independent_attrib]]
            else:
                raise ValueError("Invalid relationship type")

            # Scale the independent values
            min_ind_val = min(self.data[independent_attrib])
            max_ind_val = max(self.data[independent_attrib])
            scaled_independent_values = [(x - min_ind_val) / (max_ind_val - min_ind_val) * (independent_max_val - independent_min_val) + independent_min_val for x in self.data[independent_attrib]]

            # Scale the dependent values
            if dependent_values:  # Check if dependent_values is not empty
                min_dep_val = min(dependent_values)
                max_dep_val = max(dependent_values)
                scaled_dependent_values = [(x - min_dep_val) / (max_dep_val - min_dep_val) * (max_val - min_val) + min_val for x in dependent_values]
            else:
                scaled_dependent_values = []  # Define scaled_dependent_values as an empty list if dependent_values is empty

            # Update the data with the scaled values
            self.data[independent_attrib] = scaled_independent_values
            self.data[dependent_attrib] = scaled_dependent_values

        return self.data
