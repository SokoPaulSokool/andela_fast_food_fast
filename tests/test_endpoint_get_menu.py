import unittest
from app import Order, CustomerOrders, app
import json


class TestGetOrders(unittest.TestCase):

    def test_get_all_endpoint(self):
        test_client = app.test_client()
        response = test_client.get('/api/v1/menu')
        self.assertGreater(len(json.loads(response.data)), 0)
