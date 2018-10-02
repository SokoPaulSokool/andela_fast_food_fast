import unittest
from app import Order, CustomerOrders, app
import json


class TestDeleteOrderById(unittest.TestCase):

    def test_delete_existing_order(self):
        order = json.dumps(dict(
            item_id="1", delivery_location="delivery_location"))

        test_client = app.test_client()
        test_client.post('/api/v1/orders', data=order,
                         content_type='application/json')
        response = test_client.delete('/api/v1/orders/1')
        self.assertEqual(json.loads(response.data)[
                         "message"], "deleted")

    def test_delete_non_existing_order(self):
        test_client = app.test_client()
        response = test_client.delete('/api/v1/orders/100')
        self.assertEqual(json.loads(response.data)[
            "message"], "order does not exist")
