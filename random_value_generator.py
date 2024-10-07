"""In this module, we are generating random values for the attributes with the constraints given.
here, the constraints are range functions so this module gets synthetic data as random values in between the range set by the user."""

import random
class random_value_generator:
    def __init__(self, attr, min_val, max_val):
        self.attr = attr
        self.min_val = min_val
        self.max_val = max_val

    def generate_random_value(self):
        # Calculate a random value within the range constraints
        value = random.uniform(self.min_val, self.max_val)
        return value
