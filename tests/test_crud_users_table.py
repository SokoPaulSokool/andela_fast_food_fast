import unittest
from app.api.models.database.all_tables_create_drop import create_tables
from app.api.models.database.crud_users_table import QueryUsersTable

from app.api.models.user_manage import User


class TestUsersTable(unittest.TestCase):
    def setUp(self):
        create_tables().users_drop_table()
        create_tables().users_table()

    def teardown(self):
        create_tables().users_drop_table()

    def test_add_user(self):
        result = QueryUsersTable().add_user(
            User(1, "soko", "sopapaso73@gmail.com", "1234", "admin"))
        self.assertEqual(result[1], "soko")

    def test_add_existing_user(self):
        QueryUsersTable().add_user(
            User(1, "soko", "sopapaso73@gmail.com", "1234", "admin"))
        result = QueryUsersTable().add_user(
            User(1, "soko", "sopapaso73@gmail.com", "1234", "admin"))
        self.assertEqual(result, "user exists")

    def test_get_existing_user_by_email(self):
        usersTable = QueryUsersTable()
        usersTable.add_user(
            User(1, "soko", "sopapaso73@gmail.com", "1234", "admin"))
        result = usersTable.get_user_by_email("sopapaso73@gmail.com")
        self.assertEqual(result[1], "soko")

    def test_non_get_existing_user_by_email(self):
        usersTable = QueryUsersTable()
        result = usersTable.get_user_by_email("sopapaso73@gmail.com")
        self.assertEqual(result, "failed")

    def test_delete_existing_user_by_email(self):
        usersTable = QueryUsersTable()
        usersTable.add_user(
            User(1, "soko", "sopapaso73@gmail.com", "1234", "admin"))
        result = usersTable.delete_user_by_email("sopapaso73@gmail.com")
        self.assertEqual(result, 1)

    def test_delete_non_existing_user_by_email(self):
        usersTable = QueryUsersTable()
        result = usersTable.delete_user_by_email("sopapaso73@gmail.com")
        self.assertEqual(result, 0)
