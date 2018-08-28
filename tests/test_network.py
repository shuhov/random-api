import unittest
from urlparse import urljoin

import requests


class NetworkResourceTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/api/v1/random/network"
        self.headers = {'Content-type': 'application/json'}

    def test_get_list_of_all_network_resources(self):
        pass

    def test_get_ipv4(self):
        url = urljoin(self.base_url, 'ipv4_address')
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

        resource = response.json()
        print(resource)
        self.assertEqual(resource['name'], 'ip_address')
