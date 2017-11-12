from flask_restful import fields


class IPv4Fields:

    resource_fields = {
        'name': fields.String,
        'value': fields.String
    }

