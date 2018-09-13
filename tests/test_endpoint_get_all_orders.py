import unittest
from app import Order, CustomerOrders, app
import json


class TestApis(unittest.TestCase):

    def test_get_all_endpoint(self):
        response = app.test_client().get('/api/v1/orders')
        self.assertEqual(json.loads(response.data), [])
