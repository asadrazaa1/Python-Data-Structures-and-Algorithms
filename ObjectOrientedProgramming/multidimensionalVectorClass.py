"""
Demonstrate the use of operator overloading via special methods, we provide
an implementation of a Vector class, representing the coordinates of a vector in a
multidimensional space.
"""


class Vector():
    """Represent a vector in a multidimensional space"""

    def __init__(self, d) -> None:
        """Create a d-dimensional vector of zeros"""
        self._coords = [0]*d
    
    def __len__(self):
        """Return the dimension of a vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self._coords[j] + other[j]
        return result

    def __eq__(self, __o: object) -> bool:
        """Return True if vector has same coordinates as other."""
        return self._coords == __o
    
    def __ne__(self, __o: object) -> bool:
        """Return True if vector differs from other."""
        return not self._coords == __o

    def __str__(self) -> str:
        """Produce string representation of vector."""
        return '<' + str(self._coords[1:-1]) + '>'