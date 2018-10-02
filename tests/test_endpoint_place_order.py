import unittest
from app import Order, CustomerOrders, app, OrderItem, Menu
import json
import pytest
from app.api.models.user_manage import User
from app.api.models.database.crud_orders_table import QueryOrdersTable
from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.database.crud_users_table import QueryUsersTable
from app.api.models.database.all_tables_create_drop import create_tables


class OrdersHelpers():

    def __init__(self, app):
        self.test_client = app.test_client()

    def signup_get_token(self):
        self.test_client.post('/api/v1/auth/signup',
                              data=dict(user_name="user_name",
                                        email="sopapaso73@gmail.com",
                                        password="password",
                                        user_type="admin"
                                        ), content_type='application/json'
                              )
        response = self.test_client.post('/api/v1/auth/login',
                                         data=dict(
                                             email="sopapaso73@gmail.com",
                                             password="password"
                                         ), content_type='application/json'
                                         )
        print(response)
        return json.loads(response.data)["message"]["access_token"]

    def add_order(self, item_id, delivery_location):
        response = self.test_client.post('/api/v1/orders', data=json.dumps(dict(
            item_id=item_id, delivery_location=delivery_location)),  headers={
            'Authorization': 'Bearer ' + self.signup_get_token()}, content_type='application/json')

        return response


@pytest.mark.parametrize("item_id, delivery_location",
                         [
                             ("", "delivery_location"),
                             (1, "")
                         ])
def test_submit_with_empty_value(item_id, delivery_location):
    pass


def test_submit_with_full_value():
    pass
