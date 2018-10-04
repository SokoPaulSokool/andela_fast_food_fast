import unittest
from app import Order, CustomerOrders, app
import json
import pytest
from tests.orders_helper import OrdersHelpers


class MenuHelpers():

    def __init__(self, app):
        self.test_client = app.test_client()

    def add_menu(self, item_name, item_description, item_price):
        token = OrdersHelpers.get_admin_token()
        response = self.test_client.post('/api/v1/menu', data=json.dumps(dict(
            item_name=item_name, item_description=item_description, item_price=item_price)),
            headers={'Authorization': 'Bearer ' + token},
            content_type='application/json')
        return response


@pytest.mark.parametrize("item_name, item_description, item_price",
                         [
                             ("", "item_description", "item_price"),
                             ("item_name", "", "item_price"),
                             ("item_name", "item_description", ""),
                         ])
def test_submit_with_empty_value(item_name, item_description, item_price):
    response = MenuHelpers(app).add_menu(
        item_name, item_description, item_price)
    message = json.loads(response.get_data(as_text=True))["message"]
    if not item_name:
        assert message == "either item_name is not set or empty"
    if not item_description:
        assert message == "either item_description is not set or empty"
    if not item_price:
        assert message == "either item_price is not set or empty"


def test_submit_with_full_value():
    response = MenuHelpers(app).add_menu("chips", "just nice", 1000)
    message = json.loads(response.get_data(as_text=True))[
        "item_name"]
    assert response.status_code == 200
