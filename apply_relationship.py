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
                slope = random.uniform(-0.1, 0.1)  # reduced range for slope
                intercept = random.uniform(-0.3, 0.3)  # reduced range for intercept
                dependent_values = [slope * x + intercept for x in self.data[independent_attrib]]
            elif relationship['type'] == 'parabolic':
                a = random.uniform(-0.2, 0.2)  # reduced range for coefficient
                h = random.uniform(-0.5, 0.5)  # reduced range for horizontal shift
                k = random.uniform(-0.4, 0.4)  # reduced range for vertical shift
                dependent_values = [a * (x - h) ** 2 + k for x in self.data[independent_attrib]]
            elif relationship['type'] == 'exponential':
                a = random.uniform(0.8, 1.2)  # modified range for coefficient
                b = random.uniform(-0.5, 0.5)  # reduced range for exponent
                dependent_values = [a * np.exp(b * x) for x in self.data[independent_attrib]]
            elif relationship['type'] == 'sinusoidal':
                a = random.uniform(-0.2, 0.2)  # reduced range for amplitude
                b = random.uniform(-0.5, 0.5)  # reduced range for frequency
                dependent_values = [a * np.sin(b * x) for x in self.data[independent_attrib]]
            elif relationship['type'] == 'hyperbolic':
                a = random.uniform(-0.2, 0.2)  # reduced range for coefficient
                b = random.uniform(-0.2, 0.2)  # reduced range for exponent
                dependent_values = [a * (1 / (1 + b * x)) for x in self.data[independent_attrib]]
            elif relationship['type'] == 'sigmoid':
                a = random.uniform(0.8, 1.2)  # modified range for coefficient
                b = random.uniform(-2, 2)  # modified range for shift
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
                denominator = max_dep_val - min_dep_val
                if denominator == 0:  # Avoid division by zero
                    denominator = 0.1 # Add a small value to the denominator
                scaled_dependent_values = [(x - min_dep_val) / denominator * (max_val - min_val) + min_val for x in dependent_values]
            else:
                scaled_dependent_values = []  # Define scaled_dependent_values as an empty list if dependent_values is empty
            # Define scaled_dependent_values as an empty list if dependent_values is empty

            # Update the data with the scaled values
            self.data[independent_attrib] = scaled_independent_values
            self.data[dependent_attrib] = scaled_dependent_values

        return self.data
