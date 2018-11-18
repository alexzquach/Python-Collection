"""
point module
"""
from typing import Any


class Point:
    """ Represent a point given by (x,y)

    x - represents the x-coordinate of the point
    y - represents the y-coordinate of the point
    """
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        """ Intializes a new point """

        # Intializes the x and y coordinates of the point object
        self.x, self.y = float(x), float(y)

    def __str__(self) -> str:
        """ Returns a string representation of the point

        >>> point_1 = Point(10, 3)
        >>> print(point_1)
        (10.0, 3.0)
        """

        # Builds a string representation of the point and returns it
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other: Any) -> bool:
        """ Returns whether self is equal to other

        >>> point_1 = Point(5, 3)
        >>> point_2 = Point(5.0, 3.0)
        >>> point_1 == point_2
        True
        >>> point_3 = (3, 5.0)
        >>> point_1 == point_3
        False
        """

        # Checks if self and other are the same type, then compares their
        # point values if they are the same type
        return (type(self) == type(other) and self.x == other.x and
                self.y == other.y)

    def distance_to_point(self, x_coordinate: float, y_coordinate: float) -> float:
        """ Returns the distance from point to another point given by
        (x_coordinate, y_coordinate) calculated using the pythagorean theorem

        >>> point_1 = Point(9, 3)
        >>> point_1.distance_to_point(1, 1)
        8.246211251235321
        """

        # Finds the distance to the point given by the user using the
        # pythagorean theorem
        return ((self.x - x_coordinate)** 2 + (self.y - y_coordinate)** 2) ** 0.5

    def distance_to_origin(self) -> float:
        """ Returns the distance from point to the origin, calculated using the
        pythagorean theorem

        >>> point_1 = Point(3, 4)
        >>> point_1.distance_to_origin()
        5.0
        """

        # Finds the distance to the origin (0,0) using the pythagorean theorem
        return (self.x ** 2 + self.y ** 2)** 0.5

    def mid_point(self, x_2: float = 0, y_2: float = 0) -> str:
        """ Returns the midpoint of the line formed by two points, with the
        origin being the default point if the user does not give any parameters

        >>> point_1 = Point(3, 4)
        >>> point_1.mid_point()
        '(1.5, 2.0)'
        """

        # Finds the mid x value and mid y value and combines them into
        # a string representation for the user
        mid_x = (self.x + x_2) / 2
        mid_y = (self.y + y_2) / 2
        return  "(" + str(mid_x) + ", " + str(mid_y) + ")"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
