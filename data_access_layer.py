from requests import get
from serializers import Employee
from models import HourlyEmployee, MonthlyEmployee
from urllib3.exceptions import HTTPError


class AccessApi(object):
    """
    Queries the api and saves data in a map that stores employees according to
    the type of contract
    """

    URL = 'http://masglobaltestapi.azurewebsites.net/api/Employees'
    HEADERS = {'Accept': 'application/json'}

    def __init__(self):
        self.employees_map = self._get_data()

    def _get_data(self) -> map:
        """
        Calls the api and stores employees in a map
        """
        response = get(url=self.URL, headers=self.HEADERS)

        if response.status_code != 200:
            raise HTTPError
        employees = Employee().load(data=response.json(), many=True)
        employees_map = map(
            lambda employee: self._employee_factory(
                employee.get('contractTypeName'), employee), employees
        )

        return employees_map

    def _employee_factory(self, contracttypename, data):
        """
        Creates employees depending on contract type
        """
        if contracttypename == 'HourlySalaryEmployee':
            return HourlyEmployee(**data)
        return MonthlyEmployee(**data)

    def filter_employee(self, employee_id):
        """
        Filrters an employee by Id
        """
        employee = filter(lambda employee: employee.id == employee_id,
                          self.employees_map)
        return employee
