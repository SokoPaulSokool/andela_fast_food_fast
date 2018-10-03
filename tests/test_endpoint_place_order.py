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

    def add_order(self, item_id, delivery_location):
        QueryUsersTable().add_user(User("", "soko", "sopapaso73@gmail.com", "1234", "admin"))
        response = self.test_client.post('/api/v1/users/orders', data=json.dumps(dict(
            item_id=item_id, delivery_location=delivery_location)),  headers={
            'Authorization': 'Bearer ' + self.get_token()}, content_type='application/json')

        return response

    def get_token(self):
        test_client = app.test_client()
        response = test_client.post('/api/v1/auth/login', data=json.dumps(dict(
            email="sopapaso73@gmail.com", password="1234",)), content_type='application/json')
        return json.loads(response.get_data(as_text=True))["message"]["access_token"]


@pytest.mark.parametrize("item_id, delivery_location",
                         [
                             ("", "delivery_location"),
                             (1, "")
                         ])
def test_submit_with_empty_value(item_id, delivery_location):
    response = OrdersHelpers(app).add_order(item_id, delivery_location)
    message = json.loads(response.get_data(as_text=True))[
        "message"]
    if not item_id:
        assert message == "either item_id is not set or empty"
    if not delivery_location:
        assert message == "either delivery_location is not set or empty"


def test_submit_with_full_value():
    response = OrdersHelpers(app).add_order(1, "kla")
    message = json.loads(response.get_data(as_text=True))[
        "message"]
    assert response.status_code == 200
