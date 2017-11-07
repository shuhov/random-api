import unittest

import requests

from project.src import app


class TicketSystemTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/api/v1/random"
        self.headers = {'Content-type': 'application/json'}

    def test_run_app(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 404)

    def test_read_config(self):
        self.assertEqual(app.config['DB_SCHEMA'], 'r_api_sys')
