"""
Models that represent Employees
"""


class BaseEmployee(object):
    """
    Represents an employee with the basic attributes from the API
    """
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.contractTypeName = kwargs['contractTypeName']
        self.roleId = kwargs['roleId']
        self.roleName = kwargs['roleName']
        self.roleDescription = kwargs['roleDescription']
        self.hourlySalary = kwargs['hourlySalary']
        self.monthlySalary = kwargs['monthlySalary']

    def __str__(self):
        return str(self.__dict__)


class HourlyEmployee(BaseEmployee):
    """
    Model for an employee with Hourly salary contract
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.annualSalary = self._hourly_to_annual(kwargs['hourlySalary'])

    def _hourly_to_annual(self, hourlysalary: int) -> int:
        return 120 * hourlysalary * 12


class MonthlyEmployee(BaseEmployee):
    """
    Model for an employee with Monthly salary contract
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.annualSalary = self._monthly_to_annual(kwargs['monthlySalary'])

    def _monthly_to_annual(self, monthlysalary: int) -> int:
        return monthlysalary * 12
