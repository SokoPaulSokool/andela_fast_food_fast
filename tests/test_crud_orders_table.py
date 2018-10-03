import unittest
from app.api.models.database.all_tables_create_drop import create_tables
from app.api.models.database.crud_orders_table import QueryOrdersTable
from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.database.crud_users_table import QueryUsersTable

from app.api.models.orders_manage import OrderItem, Menu
from app.api.models.user_manage import User


class TestOrdersTable(unittest.TestCase):
    def setUp(self):
        create_tables().orders_drop_table()
        create_tables().orders_table()

    def teardown(self):
        create_tables().orders_drop_table()

    def test_add_Order_item(self):
        QueryMenuTable().add_item(Menu("", "chicken", "fried chicken", 10000))
        QueryUsersTable().add_user(User("", "soko", "sopapaso73@gmail.com", "1234", "admin"))
        result = QueryOrdersTable().add_order(
            OrderItem("", 1, 1, "Kampala"))
        self.assertEqual(result[4], "Kampala")

    def test_geting_all_orders(self):
        QueryMenuTable().add_item(Menu("", "chicken", "fried chicken", 10000))
        QueryUsersTable().add_user(User("", "soko", "sopapaso73@gmail.com", "1234", "admin"))
        orders_table = QueryOrdersTable()
        orders_table.add_order(
            OrderItem("", 1, 1, "Kampala"))
        orders_table.add_order(
            OrderItem("", 1, 1, "Kampala"))
        orders_table.add_order(
            OrderItem("", 1, 1, "Kampala"))
        result = orders_table.get_all_orders()
        self.assertEqual(len(result), 3)

    def test_geting_all_orders_for_specific_user(self):
        QueryMenuTable().add_item(Menu("", "chicken", "fried chicken", 10000))
        QueryUsersTable().add_user(User("", "soko", "sopapaso73@gmail.com", "1234", "admin"))
        QueryUsersTable().add_user(User("", "paul", "paul@gmail.com", "1234", "admin"))
        orders_table = QueryOrdersTable()
        orders_table.add_order(
            OrderItem("", 1, 1, "Kampala"))
        orders_table.add_order(
            OrderItem("", 2, 1, "Kampala"))
        orders_table.add_order(
            OrderItem("", 2, 1, "Kampala"))
        result = orders_table.get_all_orders_for_user(2)
        print(result)
        self.assertEqual(len(result), 2)

    def test_geting_order_by_id(self):
        QueryMenuTable().add_item(Menu("", "chicken", "fried chicken", 10000))
        QueryUsersTable().add_user(User("", "soko", "sopapaso73@gmail.com", "1234", "admin"))
        QueryUsersTable().add_user(User("", "paul", "paul@gmail.com", "1234", "admin"))
        orders_table = QueryOrdersTable()
        orders_table.add_order(
            OrderItem("", 1, 1, "Kampala"))
        orders_table.add_order(
            OrderItem("", 2, 1, "Kampala"))
        orders_table.add_order(
            OrderItem("", 2, 1, "Kampala"))
        result = orders_table.get_order_by_id(2)
        print(result)
        self.assertEqual(result[0], 2)
