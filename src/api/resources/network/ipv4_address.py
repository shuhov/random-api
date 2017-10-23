import random
import socket
import struct

from flask import jsonify, make_response
from flask_restful import Resource, reqparse


class IPv4Address(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('mask', type=int, location='json')
        self.reqparse.add_argument('from', type=str, location='json')
        self.reqparse.add_argument('to', type=str, location='json')
        super(IPv4Address, self).__init__()
        self.name = 'ip_address'

    def get(self):
        ip_address = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        data = {
            'resource': {
                'name': 'ip_address',
                'value': ip_address,
            }
        }
        return make_response(jsonify(data=data), 200)
