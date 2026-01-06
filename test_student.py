from student import get_student_result

def test_grade_S():
    expected_output = (
        "Name: anannya, Department: bca, Semester: 3, "
        "Average: 90.00, Grade: S"
    )
    assert get_student_result("anannya", "bca", "3", 95, 90, 85) == expected_output


def test_grade_A():
    expected_output = (
        "Name: anannya, Department: bca, Semester: 3, "
        "Average: 82.33, Grade: A"
    )
    assert get_student_result("anannya", "bca", "3", 85, 80, 82) == expected_output


def test_grade_B():
    expected_output = (
        "Name: anannya, Department: bca, Semester: 3, "
        "Average: 71.00, Grade: B"
    )
    assert get_student_result("anannya", "bca", "3", 70, 68, 75) == expected_output


def test_grade_C():
    expected_output = (
        "Name: anannya, Department: bca, Semester: 3, "
        "Average: 57.67, Grade: C"
    )
    assert get_student_result("anannya", "bca", "3", 55, 60, 58) == expected_output


def test_grade_D():
    expected_output = (
        "Name: anannya, Department: bca, Semester: 3, "
        "Average: 42.33, Grade: D"
    )
    assert get_student_result("anannya", "bca", "3", 40, 45, 42) == expected_output


def test_grade_F():
    expected_output = (
        "Name: anannya, Department: bca, Semester: 3, "
        "Average: 34.33, Grade: F"
    )
    assert get_student_result("anannya", "bca", "3", 30, 35, 38) == expected_output
