"""In this module, for each attribute we collect a range constraint.
these constraints are collected so that when synthetic data is generated the value stay between these range """

class Constraints_Calculator:
    def __init__(self, attributes):
        self.attributes = attributes

    def get_constraints(self, constraints):
        for attr in self.attributes:
            while True:
                constraint = constraints[attr]
                if constraint:
                    break
                else:
                    raise ValueError("Constraint must be provided for each attribute")
        return constraints

