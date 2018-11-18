"""
grade.py tester
"""

import grade

if __name__ == '__main__':
    grades = ([grade.NumericGradeEntry('CSC148', 0.5, 87.0), grade.NumericGradeEntry(
        'MAT137', 1.0, 76.0), grade.LetterGradeEntry('EAS120', 0.5, 'B+')])

    for g in grades:
        print("Weight: {}, grade: {}, points: {}".format(g.course_weight * 2.0, g.grade, g.point))

    total = sum([g.point * g.course_weight * 2.0 for g in grades])
    total_weight = sum(g.course_weight * 2.0 for g in grades)
    print("GPA = {}".format(total / total_weight))
