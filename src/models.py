import random
import socket
import struct


class IPv4:
    name = 'ip_address'
    value = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))