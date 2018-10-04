import unittest
from app import Order, CustomerOrders, app
import json
from app import Order, CustomerOrders, app,  OrderItem, Menu
import json
from app.api.models.user_manage import User
from app.api.models.database.crud_orders_table import QueryOrdersTable
from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.database.crud_users_table import QueryUsersTable
from app.api.models.database.all_tables_create_drop import create_tables
from tests.orders_helper import OrdersHelpers


class TestGetOrdersById(unittest.TestCase):
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
        CustomerOrders().place_order(self.order)

    def teardown(self):
        create_tables().users_drop_table()
        create_tables().menu_drop_table()
        create_tables().orders_drop_table()

    def test_get_existing_order(self):
        order = json.dumps(dict(
            item_id="1", delivery_location="delivery_location"))
        token = OrdersHelpers.get_admin_token()
        test_client = app.test_client()
        test_client.post('/api/v1/orders', data=order,  headers={'Authorization': 'Bearer ' + token},
                         content_type='application/json')
        response = test_client.get(
            '/api/v1/orders/1', headers={'Authorization': 'Bearer ' + token})
        # self.assertAlmostEqual(json.loads(
        #     response.get_data(as_text=True)), "1")

    def test_get_non_existing_order(self):
        test_client = app.test_client()
        response = test_client.get('/api/v1/orders/100')
