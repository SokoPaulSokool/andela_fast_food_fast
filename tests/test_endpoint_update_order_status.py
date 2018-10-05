import unittest
from app import Order, CustomerOrders, app,  OrderItem, Menu
import json
from app.api.models.user_manage import User
from app.api.models.database.crud_orders_table import QueryOrdersTable
from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.database.crud_users_table import QueryUsersTable
from app.api.models.database.all_tables_create_drop import create_tables


class TestUpdateOrderStatus(unittest.TestCase):
    def setUp(self):
        create_tables().users_drop_table()
        create_tables().menu_drop_table()
        create_tables().orders_drop_table()
        create_tables().users_table()
        create_tables().menu_table()
        create_tables().orders_table()
        QueryMenuTable().add_item(Menu("", "chicken", "fried chicken", 10000))
        QueryUsersTable().add_user(
            User("", "soko", "sopapaso73@gmail.com", "password", "admin"))
        self.order = OrderItem("", 1, 1, "kla")
        CustomerOrders().place_order(self.order)

    def teardown(self):
        create_tables().users_drop_table()
        create_tables().menu_drop_table()
        create_tables().orders_drop_table()

    def get_token(self):
        test_client = app.test_client()
        response = test_client.post('/api/v1/auth/login', data=json.dumps(dict(
            email="sopapaso73@gmail.com", password="password",)), content_type='application/json')
        return json.loads(response.get_data(as_text=True))["access_token"]

    def test_sending_empty_order_status(self):
        test_client = app.test_client()
        response = test_client.put('/api/v1/orders/1', data=json.dumps(dict(
            order_status="")), content_type='application/json', headers={
                'Authorization': 'Bearer ' + self.get_token()})

        self.assertEqual(json.loads(response.data)[
                         "message"], "either order_status is not set or empty")

    def test_updating_non_existing_order(self):
        test_client = app.test_client()
        response = test_client.put('/api/v1/orders/20', data=json.dumps(dict(
            order_status="complete")), content_type='application/json', headers={
                'Authorization': 'Bearer ' + self.get_token()})

        self.assertEqual(json.loads(response.data)[
                         "message"], "order does not exist")

    def test_updating_existing_order(self):
        test_client = app.test_client()
        response = test_client.put('/api/v1/orders/1', data=json.dumps(dict(
            order_status="complete")), content_type='application/json', headers={
                'Authorization': 'Bearer ' + self.get_token()})

        self.assertEqual(json.loads(response.data)[
                         "message"], "status changed to complete")
