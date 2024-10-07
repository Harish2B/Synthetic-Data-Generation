"""
In this module, the random value generator class is used to generate the synthetic data for the attributes with their constraints given by the user.
"""
from random_value_generator import random_value_generator


class synthetic_data_generation:
    def __init__(self, attributes, num_records, constraints):
        self.attributes = attributes
        self.num_records = num_records
        self.constraints = constraints

    # To create a synthetic data generation with the relationships
    def synthetic_data_generator(self):
        data = {}

        # Initialize attributes with random values within constraints
        for attr in self.attributes:
            # Accessing constraints correctly
            min_val = self.constraints[attr]['min']
            max_val = self.constraints[attr]['max']
            random_generator = random_value_generator(attr, min_val, max_val)
            data[attr] = []
            for _ in range(self.num_records):
                value = random_generator.generate_random_value()
                data[attr].append(value)

        return data
