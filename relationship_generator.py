"""
In this module, we get the user input on what attribute they are considering as independent attribute and what attribute they consider as dependent attribute.
then we ask in what relationship does the dependent attribute and independent attribute should be.
once we get these values, we calculate the relationship in apply_relationship module
"""

class relationship_generator:
    def __init__(self, attributes):
        self.attributes = attributes

    @staticmethod
    def get_relationship(relationships):
        return relationships
