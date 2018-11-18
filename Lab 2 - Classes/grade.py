"""
Grades module
"""

from typing import Any


class GradeEntry:
    """
    A student record system at U of T consisting of a course identifier,
    course weight and a course grade

    course_id - The course identifier, such as "CSC165".
    course_weight - The weight of the course, 0.5 for a half course, 2.0 credits
    for a full course
    """
    course_id: str
    course_weight: float

    def __init__(self, c_id: str, weight: float) -> None:
        """ Represent a grade entry for a student record system """

        # Intializes the grade entry
        self.course_id, self.course_weight = c_id, weight

    def __str__(self) -> str:
        """ String representation of GradeEntry """
        raise NotImplementedError("Must implement a subclass!")

    def __eq__(self, other: Any) -> bool:
        """ Return whether self is equivalent to other """
        raise NotImplementedError("Must implement a subclass!")

    def __repr__(self) -> str:
        """ Return a string representation that would evaluate
        to an equivalent GradeEntry to self

        >>> GradeEntry("CSC165", 0.5).__repr__()
        'GradeEntry(CSC165, 0.5)'
        """

        return "GradeEntry({}, {})".format(self.course_id, self.course_weight)


class LetterGradeEntry(GradeEntry):
    """
    A course grade entry with letter grades, extends GradeEntry

    letter_grade - Letter representation of the persons grade
    """
    letter_grade: str

    def __init__(self, c_id: str, weight: float, grade: str) -> None:
        """ Create a GradeEntry with a letter grade entry.  Extends GradeEntry

        >>> gr_1 = LetterGradeEntry("CSC165", 0.5, "B+")
        >>> print(gr_1)
        Course Title: CSC165. Course Weight: 0.5. Course Grade: B+. GPA: 3.3
        """

        GradeEntry.__init__(self, c_id, weight)
        self.grade = grade
        if self.grade == "A+" or self.grade == "A":
            self.point = 4.0
        elif self.grade == "A-":
            self.point = 3.7
        elif self.grade == "B+":
            self.point = 3.3
        elif self.grade == "B":
            self.point = 3.0
        elif self.grade == "B-":
            self.point = 2.7
        elif self.grade == "C+":
            self.point = 2.3
        elif self.grade == "C":
            self.point = 2.0
        elif self.grade == "C-":
            self.point = 1.7
        elif self.grade == "D+":
            self.point = 1.3
        elif self.grade == "D":
            self.point = 1.0
        elif self.grade == "D-":
            self.point = 0.7
        elif self.grade == "F":
            self.point = 0.0
        self._invariant()

    def __str__(self) -> str:
        """ Return a string representation of LetterGradeEntry

        >>> gr_1 = LetterGradeEntry('CSC165', 0.5, 'B+')
        >>> print(gr_1)
        LetterGradeEntry- Course Title: CSC165. Course Weight: 0.5. Course Grade: B+. GPA: 3.3
        """

        self._invariant()
        return (type(self).__name__ +
                '- Course Title: {}. Course Weight: {}. '
                'Course Grade: {}. GPA: {}'
                .format(self.course_id, self.course_weight, self.grade,
                        self.point))

    def __eq__(self, other: Any) -> bool:
        """ Returns true iff self is equivalent to other

        >>> gr_1 = LetterGradeEntry('CSC165', 0.5, 'A+')
        >>> gr_2 = LetterGradeEntry('CSC148', 1.0, 'A+')
        >>> gr_1 == gr_2
        False
        >>> gr_3 = LetterGradeEntry('CSC165', 0.5, 'A+')
        >>> gr_4 = LetterGradeEntry('CSC165', 0.5, 'A+')
        >>> gr_3 == gr_4
        True
        """

        self._invariant()
        return (type(self) == type(other) and self.course_id ==
                other.course_id and self.course_weight ==
                other.course_weight and self.grade == other.grade)

    def _invariant(self) -> None:
        # Quit if the letter grade is not proper
        assert self.grade in ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'], "Invalid grade: {}".format(self.letter_grade)


class NumericGradeEntry(GradeEntry):
    """
    A course grade entry with numeric grades, extends GradeEntry

    letter_grade - Letter representation of the persons grade
    """
    letter_grade: str

    def __init__(self, c_id: str, weight: float, grade: float) -> None:
        """ Create a GradeEntry with a letter grade entry.  Extends GradeEntry

        >>> gr_1 = NumericGradeEntry("CSC165", 0.5, 100.0)
        >>> print(gr_1)
        Course Title: CSC165. Course Weight: 0.5. Course Grade: 100.0. GPA: 4.0
        """

        GradeEntry.__init__(self, c_id, weight)
        self.grade = float(grade)
        if 100.0 >= round(self.grade, 0) >= 85.0:
            self.point = 4.0
        elif 84.0 >= round(self.grade, 0) >= 80.0:
            self.point = 3.7
        elif 79.0 >= round(self.grade, 0) >= 77.0:
            self.point = 3.3
        elif 76.0 >= round(self.grade, 0) >= 73.0:
            self.point = 3.0
        elif 72.0 >= round(self.grade, 0) >= 70.0:
            self.point = 2.7
        elif 69.0 >= round(self.grade, 0) >= 67.0:
            self.point = 2.3
        elif 66.0 >= round(self.grade, 0) >= 63.0:
            self.point = 2.0
        elif 62.0 >= round(self.grade, 0) >= 60.0:
            self.point = 1.7
        elif 59.0 >= round(self.grade, 0) >= 57.0:
            self.point = 1.3
        elif 56.0 >= round(self.grade, 0) >= 53.0:
            self.point = 1.0
        elif 52.0 >= round(self.grade, 0) >= 50.0:
            self.point = 0.7
        elif 49.0 >= round(self.grade, 0) >= 0:
            self.point = 0.0
        self._invariant()

    def __str__(self) -> str:
        """ Return a string representation of LetterGradeEntry

        >>> gr_1 = NumericGradeEntry('CSC165', 0.5, 76.0)
        >>> print(gr_1)
        NumericGradeEntry- Course Title: CSC165. Course Weight: 0.5. Course Grade: 76.0. GPA: 3.0
        """

        self._invariant()
        return (type(self).__name__ + '- Course Title: {}. Course Weight: {}. Course Grade: {}. GPA: {}'
                .format(self.course_id, self.course_weight, self.grade,
                        self.point))

    def __eq__(self, other: Any) -> bool:
        """ Returns true iff self is equivalent to other

        >>> gr_1 = NumericGradeEntry('CSC165', 0.5, 97.0)
        >>> gr_2 = NumericGradeEntry('CSC148', 1.0, 97.0)
        >>> gr_1 == gr_2
        False
        >>> gr_3 = NumericGradeEntry('CSC165', 0.5, 97.0)
        >>> gr_4 = NumericGradeEntry('CSC165', 0.5, 97.0)
        >>> gr_3 == gr_4
        True
        """

        self._invariant()
        return (type(self) == type(other) and self.course_id ==
                other.course_id and self.course_weight ==
                other.course_weight and self.grade == other.grade)

    def _invariant(self) -> None:
        # Quit if the letter grade is not proper
        assert type(self.grade) == float and self.grade in range(0, 101), "Invalid grade: {}".format(self.grade)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
