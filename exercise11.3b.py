# exercise11.3/test_employee.py (with fixture)

import pytest
 
from employee import Employee
 
 
@pytest.fixture
def employee():
    """An employee that will be available to all test functions."""
    return Employee('budi', 'santoso', 65000)
 
 
def test_give_default_raise(employee):
    """Does a default raise of $5,000 work?"""
    employee.give_raise()
    assert employee.annual_salary == 70000
 
 
def test_give_custom_raise(employee):
    """Does a custom raise of $10,000 work?"""
    employee.give_raise(10000)
    assert employee.annual_salary == 75000