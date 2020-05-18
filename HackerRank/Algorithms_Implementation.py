# https://www.hackerrank.com/challenges/grading/problem
# Grading Students


def gradingStudents(grades):
    # Write your code here
    for i, grade in enumerate(grades):
        if grade >= 38:
            rest = grade % 5
            grade += 5 - rest if rest > 2 else 0
            grades[i] = grade
    return grades

############################################################################################
# https://www.hackerrank.com/challenges/kangaroo/problem
# Kangaroo

def kangaroo(x1, v1, x2, v2):
    if x1 > x2 and v1 > v2:
        x1, x2, v1, v2 = x2, x1, v2, v1
    if x1 > x2 and v1 > v2:
        return "NO"
    if x2 > x1 and v2 > v1:
        return "NO"
    if v2 == v1:
        return "NO"
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

############################################################################################