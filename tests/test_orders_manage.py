import unittest
from app import Order, CustomerOrders, OrderItem, Menu
from app.api.models.user_manage import User
from app.api.models.database.crud_orders_table import QueryOrdersTable
from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.database.crud_users_table import QueryUsersTable
from app.api.models.database.all_tables_create_drop import create_tables


class TestOrders(unittest.TestCase):
    def setUp(self):
        create_tables().users_drop_table()
        create_tables().menu_drop_table()
        create_tables().orders_drop_table()
        create_tables().users_table()
        create_tables().menu_table()
        create_tables().orders_table()
        QueryMenuTable().add_item(Menu("", "chicken", "fried chicken", 10000))
        QueryUsersTable().add_user(User("", "soko", "sopapaso73@gmail.com", "1234", "admin"))
        self.order = OrderItem("", 1, 1, "kla")
        self.orders_list = CustomerOrders()

    def teardown(self):
        create_tables().users_drop_table()
        create_tables().menu_drop_table()
        create_tables().orders_drop_table()

    def test_order_instance(self):
        self.assertIsInstance(self.order, OrderItem)

    def test_invalid_order_instance(self):
        with self.assertRaises(TypeError):
            OrderItem("order_title", "order_description",
                      "order_price")

    def test_order_list_instance(self):
        self.assertIsInstance(self.orders_list, CustomerOrders)

    def test_place_single_order(self):
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.get_all_orders()), 1)
        self.assertEqual(self.orders_list.get_all_orders()[0]["order_id"], 1)

    def test_place_multiple_order(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.get_all_orders()), 3)
        self.assertEqual(self.orders_list.get_all_orders()[2]["order_id"], 3)

    def test_getting_all_orders(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.get_all_orders()), 3)

    def test_getting_order_by_id(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(
            1)["delivery_location"], str(self.order.delivery_location))

    def test_getting_order_by_id_that_that_does_not_exist(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(10),
                         "order does not exist")

    def test_deleting_order_by_id(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.delete_order(2), "deleted")
        self.assertEqual(len(self.orders_list.get_all_orders()), 1)

    def test_deleting_order_by_id_that_that_does_not_exist(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.delete_order(10),
                         "order does not exist")
        self.assertEqual(len(self.orders_list.get_all_orders()), 2)

    def test_changing_order_status(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            1, "pending"), "status changed to pending")
        self.assertEqual(self.orders_list.get_order(1)
                         ["order_status"], "pending")

    def test_changing_order_status_of_oder_that_does_not_exist(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            100, "pending"), "order does not exist")
