from data_access_layer import AccessApi
from forms import GetUserInputForm
from flask import render_template, Blueprint, request
from urllib3.exceptions import HTTPError
from requests.exceptions import ConnectionError
from marshmallow.exceptions import ValidationError

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = GetUserInputForm()
    employee_list = []
    message = ''
    if request.method == 'POST':
        try:
            data = AccessApi()
        except (HTTPError, ConnectionError):
            message = 'Network Error, please try again later'
        except ValidationError:
            message = 'Data types from API with wrong format'
        else:
            employee_id = form.employee_id.data
            if employee_id:
                employee_list = data.filter_employee(employee_id)
            else:
                employee_list = data.employees_map
    return render_template('index.html',
                           form=form,
                           employees=employee_list,
                           message=message)
