import random
import socket
import struct

from flask import request
from flask_restplus import Namespace, Resource

from src.common.database import get_connection
from src.api.resources.network.models import model

api = Namespace('network', description='Random network data')


class IPv4Address(Resource):

    @api.marshal_with(model)
    def get(self):
        name = 'ip_address'
        value = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        conn = get_connection()
        sql = """INSERT INTO public.resources
                    (name, value, user_agent)
                 VALUES (%(name)s, %(value)s, %(user_agent)s)
                 RETURNING *"""
        bindings = {
            'name': name,
            'value': value,
            'user_agent': request.headers.get('User-Agent'),
        }
        conn.execute(sql, bindings, commit=True)
        return {'name': name, 'value': value}


