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
        self.assertEqual(self.orders_list.orders_list[0].order_id, 1)

    def test_place_multiple_order(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.orders_list), 3)
        self.assertEqual(self.orders_list.orders_list[2].order_id, 3)

    def test_getting_all_orders(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.get_all_orders()), 3)

    def test_getting_order_by_id(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(1), self.order)

    def test_getting_order_by_id_that_that_does_not_exist(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(3),
                         "order does not exist")

    def test_deleting_order_by_id(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.delete_order(1), "deleted")
        self.assertEqual(len(self.orders_list.get_all_orders()), 1)

    def test_deleting_order_by_id_that_that_does_not_exist(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.delete_order(3),
                         "order does not exist")
        self.assertEqual(len(self.orders_list.get_all_orders()), 2)

    def test_changing_order_status(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            1, "pending"), "status changed to pending")
        self.assertEqual(self.orders_list.get_order(1).order_status, "pending")

    def test_changing_order_status_of_oder_that_does_not_exist(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            4, "pending"), "order does not exist")
