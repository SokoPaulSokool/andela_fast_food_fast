import unittest
from app import Order


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.order = Order("order_title", "order_description",
                           "order_price", "delivery_location")

    def teardown(self):
        pass

    def test_order_instance(self):
        self.assertIsInstance(self.order, Order)

    def test_invalid_order_instance(self):
        with self.assertRaises(TypeError):
            Order("order_title", "order_description",
                  "order_price")
