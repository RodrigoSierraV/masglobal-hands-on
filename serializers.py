from marshmallow import Schema, fields, post_load, INCLUDE


class Employee(Schema):
    """
    Serializer that receives data from the api and verifies each field type
    """

    class Meta:
        """
        Accepts other fields and include them.
        This is added to have the roleDescription field when is null
        """
        unknown = INCLUDE

    id = fields.Integer()
    name = fields.Str()
    contractTypeName = fields.Str()
    roleId = fields.Integer()
    roleName = fields.Str()
    hourlySalary = fields.Float()
    monthlySalary = fields.Float()
