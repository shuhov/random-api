import random
import socket
import struct

from flask_restplus import Resource
from random_api.api.resources.network import ns_network
from random_api.api.resources.network.models import model


@ns_network.route("/ipv4_address")
class IPv4Address(Resource):
    @ns_network.marshal_with(model)
    def get(self):
        name = "ip_address"
        value = socket.inet_ntoa(struct.pack(">I", random.randint(1, 0xFFFFFFFF)))
        return {"name": name, "value": value}
