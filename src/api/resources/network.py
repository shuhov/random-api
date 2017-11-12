from flask import request

from flask_restful import Resource, reqparse
from flask_restful import marshal
from src.common.fields import IPv4Fields

from src.models import IPv4
from src.common.database import get_connection


class IPv4Address(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('mask', type=int, location='json')
        self.reqparse.add_argument('from', type=str, location='json')
        self.reqparse.add_argument('to', type=str, location='json')
        super(IPv4Address, self).__init__()
        self.name = 'ip_address'

    def get(self):
        ipv4 = IPv4()
        conn = get_connection()
        sql = """INSERT INTO public.resources
                    (name, value, user_agent)
                 VALUES (%(name)s, %(value)s, %(user_agent)s)
                 RETURNING *"""
        bindings = {
            'name': ipv4.name,
            'value': ipv4.value,
            'user_agent': request.headers.get('User-Agent'),
        }
        conn.execute(sql, bindings, commit=True)
        return marshal(ipv4, IPv4Fields.resource_fields), 200



