from flask_restful import Resource, reqparse
from flask_restful import marshal
from project.src.models import IPv4

from project.src.common.serializers import IPv4Serializer


class IPv4Address(Resource):
    docs = {
        'tags': ['IPv4Address'],
        'description': 'Returns a random IPv4Address',
        'parameters': [
            {
                'name': 'subnet mask',
                'description': 'logical subdivision of an IP network',
                'type': 'integer'
            }
        ],
        'responses': {
            '200': {
                'description': 'IPv4Address',
                "resource": {
                    "name": "ip_address",
                    "value": "random ipv4 address"
                }
            }
        }
     }
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('mask', type=int, location='json')
        self.reqparse.add_argument('from', type=str, location='json')
        self.reqparse.add_argument('to', type=str, location='json')
        super(IPv4Address, self).__init__()
        self.name = 'ip_address'

    def get(self):
        return marshal(IPv4(), IPv4Serializer()), 200
        # return make_response(jsonify(data=data), 200)


