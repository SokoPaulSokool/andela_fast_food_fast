import unittest
from app import Order, CustomerOrders


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.order = Order("order_title", "order_description",
                           "order_price", "delivery_location")
        self.orders_list = CustomerOrders()

    def teardown(self):
        pass

    def test_order_instance(self):
        self.assertIsInstance(self.order, Order)

    def test_invalid_order_instance(self):
        with self.assertRaises(TypeError):
            Order("order_title", "order_description",
                  "order_price")

    def test_order_list_instance(self):
        self.assertIsInstance(self.orders_list, CustomerOrders)

    def test_place_single_order(self):
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.orders_list), 1)
        self.assertEqual(self.orders_list.orders_list[0].order_id, 0)

    def test_place_multiple_order(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.orders_list), 3)
        self.assertEqual(self.orders_list.orders_list[2].order_id, 2)
