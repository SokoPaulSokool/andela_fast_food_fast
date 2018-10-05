from app import Order, CustomerOrders, app
import json
from app.api.models.database.crud_users_table import QueryUsersTable
from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.database.crud_orders_table import QueryOrdersTable
from app.api.models.user_manage import User
from app.api.models import Menu
from app.api.models.database.all_tables_create_drop import create_tables


class OrdersHelpers():

    def __init__(self, app):
        self.test_client = app.test_client()
        QueryMenuTable().add_item(
            Menu("", "chicken", "fried chicken", 10000))
        QueryMenuTable().add_item(
            Menu("", "chicken", "chips", 10000))
        QueryMenuTable().add_item(
            Menu("", "chicken", "juice", 10000))

    def add_order(self, item_id, delivery_location, token):
        QueryUsersTable().add_user(
            User("", "soko", "sopapaso73@gmail.com", "password", "customer"))
        response = self.test_client.post('/api/v1/users/orders', data=json.dumps(dict(
            item_id=item_id, delivery_location=delivery_location)),  headers={
            'Authorization': 'Bearer ' + token}, content_type='application/json')
        return response

    def get_all_order(self, token):
        self.add_order(1, "kampala", token)
        self.add_order(1, "kampala", token)
        QueryUsersTable().add_user(
            User("", "soko", "sopapaso73@gmail.com", "password", "admin"))
        response = self.test_client.get(
            '/api/v1/orders', headers={'Authorization': 'Bearer ' + token})
        return response

    def get_users_orders(self, token):
        self.add_order(1, "kampala", token)
        self.add_order(1, "kampala", token)
        QueryUsersTable().add_user(
            User("", "soko", "sopapaso73@gmail.com", "password", "admin"))
        response = self.test_client.get(
            '/api/v1/users/orders', headers={'Authorization': 'Bearer ' + token})
        return response

    @staticmethod
    def get_admin_token():
        QueryUsersTable().add_user(
            User("", "soko", "sopapaso@gmail.com", "password", "admin"))
        test_client = app.test_client()
        response = test_client.post('/api/v1/auth/login', data=json.dumps(dict(
            email="sopapaso@gmail.com", password="password",)), content_type='application/json')
        print(json.loads(response.get_data(as_text=True)))
        return json.loads(response.get_data(as_text=True))["access_token"]

    @staticmethod
    def get_customer_token():
        QueryUsersTable().add_user(User("", "paul", "paul@gmail.com", "password12", "customer"))
        test_client = app.test_client()
        response = test_client.post('/api/v1/auth/login', data=json.dumps(dict(
            email="paul@gmail.com", password="password12",)), content_type='application/json')
        print(json.loads(response.get_data(as_text=True)))
        return json.loads(response.get_data(as_text=True))["access_token"]
