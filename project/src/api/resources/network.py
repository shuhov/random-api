from flask_restful import Resource, reqparse
from flask_restful import marshal

from project.src.models import IPv4
from project.src.common.fields import IPv4Fields
from flask_restful_swagger import swagger


class IPv4Address(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('mask', type=int, location='json')
        self.reqparse.add_argument('from', type=str, location='json')
        self.reqparse.add_argument('to', type=str, location='json')
        super(IPv4Address, self).__init__()
        self.name = 'ip_address'

    def get(self):
        return marshal(IPv4(), IPv4Fields.resource_fields), 200


