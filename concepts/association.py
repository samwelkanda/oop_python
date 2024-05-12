"""
Association represents a broad range of relationships between objects, including
the use of one object within another. Unlike aggregation, association doesn’t
imply ownership. 
"""

class Professor:
    pass


class Department:
    def __init__(self, professor):
        self.professor = professor


# Here, Department is associated with Professor,
# but neither owns the other.