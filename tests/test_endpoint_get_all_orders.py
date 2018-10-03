import unittest
from app import Order, CustomerOrders, app
import json
from app.api.models.database.crud_users_table import QueryUsersTable
from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.database.crud_orders_table import QueryOrdersTable
from app.api.models.user_manage import User
from app.api.models import Menu
from app.api.models.database.all_tables_create_drop import create_tables
from tests.orders_helper import OrdersHelpers


class TestGetOrders(unittest.TestCase):

    def setUp(self):
        create_tables().users_drop_table()
        create_tables().menu_drop_table()
        create_tables().orders_drop_table()
        create_tables().users_table()
        create_tables().menu_table()
        create_tables().orders_table()

    def teardown(self):
        create_tables().users_drop_table()
        create_tables().menu_drop_table()
        create_tables().orders_drop_table()

    def test_get_all_orders_as_admin_endpoint(self):
        response = OrdersHelpers(app).get_all_order(
            OrdersHelpers.get_admin_token())
        self.assertEqual(len(json.loads(response.data)), 2)

    def test_get_all_orders_as_customer_endpoint(self):
        response = OrdersHelpers(app).get_all_order(
            OrdersHelpers.get_customer_token())
        self.assertEqual(json.loads(response.data)[
                         "message"], "You need to be an admin to access this route")

    def test_get_user_endpoint(self):
        response = OrdersHelpers(app).get_users_orders(
            OrdersHelpers.get_admin_token())
        self.assertEqual(len(json.loads(response.data)), 2)

    def test_get_all_orders_without_token(self):
        test_client = app.test_client()
        test_client.post('/api/v1/orders', data=json.dumps(dict(
            item_id="item_id", delivery_location="delivery_location")), content_type='application/json')
        response = test_client.get('/api/v1/orders')
        self.assertEqual(json.loads(response.data)[
                         "msg"], "Missing Authorization Header")
