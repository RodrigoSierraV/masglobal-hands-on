from wtforms import Form, IntegerField, SubmitField, validators
from flask_wtf import FlaskForm


class GetUserInputForm(FlaskForm):
    """
    Form to get user's input
    """
    employee_id = IntegerField('Employee ID',
                               render_kw={"placeholder":
                                          "Employee id (Optional)"})
    submit = SubmitField('Get Employees')
