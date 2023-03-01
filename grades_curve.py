import numpy as np

grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])

curve_center = 80


def curve_grades(grades):
    grades_avg = grades.mean()
    change = curve_center - grades_avg
    new_grades = grades + change
    # Clip (limit) the values in an array.
    # numpy.clip(a, a_min, a_max, out=None, **kwargs)
    return np.clip(new_grades, grades, 100)


print(curve_grades(grades))
