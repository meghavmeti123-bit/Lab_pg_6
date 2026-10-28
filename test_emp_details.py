

from emp_details import employee_details


def test_employee_details():
    result=employee_details("John Doe", 30, "Software Engineer", 75000)
    expected="name: John Doe, \nemployee_id: E123, \ndepartment: Software Engineer, \nsalary: 75000"
    assert result == expected