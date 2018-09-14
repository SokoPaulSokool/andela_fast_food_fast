import unittest
from app import Order, CustomerOrders, app
import json


class TestGetOrdersById(unittest.TestCase):

    def test_get_existing_order(self):
        order = json.dumps(dict(
            order_title="order_title", order_description="order_description",
            order_price="order_price", delivery_location="delivery_location"))

        test_client = app.test_client()
        test_client.post('/api/v1/orders', data=order,
                         content_type='application/json')
        response = test_client.get('/api/v1/orders/0')
        self.assertEqual(json.loads(response.data)[
                         "order_title"], "order_title")

    def test_get_non_existing_order(self):
        test_client = app.test_client()
        response = test_client.get('/api/v1/orders/3')
        self.assertEqual(json.loads(response.data)[
            "message"], "order does not exist")
