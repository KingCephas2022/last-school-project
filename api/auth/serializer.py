from flask_restx import fields



login_fields_serializer = {
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
}


register_fields_serializer = {
    'email': fields.String(required=True, description='User email address'),
    'first_name': fields.String(required=True, description="First name"),
    'last_name': fields.String(required=True, description="Lat name"),
    'password': fields.String(required=True, description="A password")}