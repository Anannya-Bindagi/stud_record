import pytest
from student import get_student_result
def test_student_grade_S():
    name = "anannya"
    dept = "bca"
    semester = "3"
    m1 = 85
    m2 = 90
    m3 = 95

    expected_output = (
        "Name: anannya, Department: bca, Semester: 3, "
        "Average: 90.00, Grade: S"
    )

    assert get_student_result(name, dept, semester, m1, m2, m3) == expected_output
