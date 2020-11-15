from marshmallow import fields, Schema, validate

nameCheck = validate.Length(min=3, error='Name is too short.')
sectorsCheck = validate.Length(min=1, error='You should choose at least one sector.')

class SelectedSectorsValidationSchema(Schema):
    id = fields.Integer(required=True)

class UserInfoValidationSchema(Schema):
    name = fields.String(validate=nameCheck, required=True)
    selected_sectors = fields.Nested(SelectedSectorsValidationSchema, many=True, required=True, validate=sectorsCheck)
    terms_agreed = fields.Boolean(required=True)