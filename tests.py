import os
import json

import unittest

from models import HourlyEmployee, MonthlyEmployee
from serializers import Employee

from marshmallow.exceptions import ValidationError
import pep8


class TestEmployees(unittest.TestCase):
    employee1 = {
        "id": 1,
        "name": "Andrea",
        "contractTypeName": "HourlySalaryEmployee",
        "roleId": 1,
        "roleName": "Administrator",
        "roleDescription": None,
        "hourlySalary": 25.0,
        "monthlySalary": 4000.0
    }

    employee2 = {
        "id": 1,
        "name": "Andrea",
        "contractTypeName": "HourlySalaryEmployee",
        "roleId": 1,
        "roleName": "Administrator",
        "roleDescription": None,
        "hourlySalary": 'a',
        "monthlySalary": 4000.0
    }

    employee3 = {
        "id": 1,
        "name": "Andrea",
        "contractTypeName": "MonthlySalaryEmployee",
        "roleId": 1,
        "roleName": "Administrator",
        "roleDescription": None,
        "hourlySalary": 30.0,
        "monthlySalary": 4800.0
    }

    def test_annual_salary(self):
        hourly_employee = HourlyEmployee(**self.employee1)
        self.assertEqual(hourly_employee.annualSalary, 36000.0)
        monthly_employee = MonthlyEmployee(**self.employee3)
        self.assertEqual(monthly_employee.annualSalary, 57600.0)

    def test_serializer(self):
        self.assertRaises(ValidationError, Employee().load, self.employee2)

if __name__ == '__main__':
    unittest.main()
