import unittest
from app.api.models.database.all_tables_create_drop import create_tables
from app.api.models.database.crud_menu_table import QueryMenuTable

from app.api.models.orders_manage import Menu


class TestMenuTable(unittest.TestCase):
    def setUp(self):
        create_tables().menu_drop_table()
        create_tables().menu_table()

    def teardown(self):
        create_tables().menu_drop_table()

    def test_add_menu_item(self):
        result = QueryMenuTable().add_item(
            Menu("", "chicken", "fried chicken", 10000))
        self.assertEqual(result[1], "chicken")

    def test_geting_item_by_id(self):
        menuTable = QueryMenuTable()
        menuTable.add_item(
            Menu("", "chicken", "fried chicken", 10000))
        result = menuTable.get_item_by_id(1)
        self.assertEqual(result[1], "chicken")

    def test_geting_all_items_on_menu(self):
        menuTable = QueryMenuTable()
        menuTable.add_item(
            Menu("", "chicken", "fried chicken", 10000))
        result = menuTable.get_all_menu_items()
        self.assertEqual(result[0][1], "chicken")

    def test_deleting_item_on_menu(self):
        menuTable = QueryMenuTable()
        menuTable.add_item(
            Menu("", "chicken", "fried chicken", 10000))
        result = menuTable.delete_item_by_id(1)
        self.assertEqual(result, 1)

    def test_deleting_non_existing_item_on_menu(self):
        menuTable = QueryMenuTable()
        result = menuTable.delete_item_by_id(1)
        self.assertEqual(result, 0)
