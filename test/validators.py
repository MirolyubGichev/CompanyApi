from django.core.exceptions import ValidationError

from djangoProject2.CompanyAPI.models import *
from unittest import TestCase

class TestCompanyModel(TestCase):

    def  test_company_name_when_input_is_valid(self):
        comapany_name = "Company"
        company = Company(
            company_name= comapany_name
        )
        self.assertIsNotNone(company.pk)

    def test_company_name_when_input_is_invalid(self):
        company_name = 'Company1'
        company = Company(
            company_name= company_name
        )

        with self.assertRaises(ValidationError) as context:
            company.full_clean()
            company.save()

        self.assertIsNotNone(context.exception)


class TestEmployeeModel(TestCase):

    def test_employee_first_name_when_input_is_valid(self):
        employee_first_name = 'Name'
        employee = Employee(
            first_name= employee_first_name
        )
        self.assertIsNotNone(employee.pk)

    def test_employee_first_name_when_input_is_invalid(self):
        employee_first_name = 'N'
        employee = Employee(
            first_name= employee_first_name
        )
        with self.assertRaises(ValidationError) as context:
            employee.full_clean()
            employee.save()

        self.assertIsNotNone(context.exception)

    def test_employee_salary_when_is_valid(self):

        employee_salary = 10
        employee = Employee(
            salary= employee_salary
        )
        self.assertIsNotNone(employee.salary)

    def test_employee_salary_when_is_invalid(self):
        employee_salary = 0
        employee = Employee(
            salary=employee_salary
        )

        with self.assertRaises(ValidationError) as context:
            employee.full_clean()
            employee.save()

        self.assertIsNotNone(context.exception)