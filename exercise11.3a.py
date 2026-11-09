# exercise11.3/test_employee.py

from employee import Employee
 
 
def test_give_default_raise():
    """Does a default raise of $5,000 work?"""
    employee = Employee('budi', 'santoso', 65000)
    employee.give_raise()
    assert employee.annual_salary == 70000
 
 
def test_give_custom_raise():
    """Does a custom raise of $10,000 work?"""
    employee = Employee('budi', 'santoso', 65000)
    employee.give_raise(10000)
    assert employee.annual_salary == 75000