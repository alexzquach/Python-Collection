"""
rational module
"""
from typing import Any


class Rational:
    """ Represent a rational number composed of the ratio between two
    integers p / q where p is the numerator and q is the denominator that cannot
    be 0

    numerator - integer numerator of the rational
    denominator - integer denominator of the rational
    """
    numerator: int
    denominator: int

    def __init__(self, numerator: int, denominator: int) -> None:
        """ Intializes a new rational """

        # Intializes the numerator and denominator of the ratio
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other: Any) -> bool:
        """ Returns true iff self is equal to other

        >>> r = Rational(3, 2)
        >>> r_2 = Rational(6, 4)
        >>> r == r_2
        True
        """

        # Checks the type then does cross multiplication to check if
        # the rationals are equal
        return (type(self) == type(other) and
                self.numerator * other.denominator ==
                self.denominator * other.numerator)

    def __str__(self) -> str:
        """ Returns the string representation of the rational

        >>> r = Rational(3, 2)
        >>> print(r)
        The rational number is: 3/2
        """

        # Builds the string representation of the rational
        return ('The rational number is: {0}/{1}'.format
                (self.numerator, self.denominator))

    def add(self, numerator: int, denominator: int) -> float:
        """ Adds two rational numbers and returns the float value that
        the addition produced

        >>> r = Rational(3, 2)
        >>> r.add(4, 2)
        3.5
        """

        # Checks if the denominators are the same
        if self.denominator == denominator:
            return (self.numerator + numerator) / denominator
        else:
            return ((self.numerator * denominator + numerator *
                     self.denominator) / (self.denominator * denominator))

    def subtract(self, numerator: int, denominator: int) -> float:
        """ Subtracts two rational numbers and returns the float value that
            the subtraction produced

        >>> r = Rational(3, 2)
        >>> r.subtract(4, 2)
        -0.5
        """

        # Checks if the denominators are the same
        if self.denominator == denominator:
            return (self.numerator - numerator) / denominator
        else:
            return ((self.numerator * denominator - numerator *
                     self.denominator) / (self.denominator * denominator))

    def multiplication(self, numerator, denominator) -> float:
        """ Multiplies the two rational numbers and returns the float
        value that the multiplication produced (rounded to two decimal points)

        >>> r = Rational(10, 90)
        >>> r.multiplication(100, 100)
        0.11
        """

        # Multiplies and rounds the resulting rational
        return (round((self.numerator * numerator) /
                      (self.denominator * denominator), 2))

    def division(self, numerator: int, denominator: int) -> float:
        """ Divides the two rational numbers and returns the float
            value that the division produced (rounded to two decimal points)

            >>> r = Rational(10, 90)
            >>> r.multiplication(100, 100)
            0.11
            """

        # Divides and rounds the resulting rational
        return (round((self.numerator * denominator) /
                      (self.denominator * numerator), 2))

    def inequality(self, numerator: int, denominator: int) -> str:
        """ Returns a string stating whether the rational is =, >, or <
        to the user given rational

        >>> r = Rational(3, 4)
        >>> r.inequality(1, 2)
        '3/4 > 1/2'
        """

        # Compares the two rationals and returns the appropriate message
        if self.numerator * denominator == self.denominator * numerator:
            return (str(self.numerator) + '/' + str(self.denominator)
                    + ' = ' + str(numerator) + '/' + str(denominator))
        elif self.numerator / self.denominator < numerator / denominator:
            return (str(self.numerator) + '/' + str(self.denominator)
                    + ' < ' + str(numerator) + '/' + str(denominator))
        else:
            return (str(self.numerator) + '/' + str(self.denominator)
                    + ' > ' + str(numerator) + '/' + str(denominator))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
