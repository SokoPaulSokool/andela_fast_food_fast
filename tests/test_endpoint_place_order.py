import unittest
from app import Order, CustomerOrders, app
import json
import pytest


@pytest.mark.parametrize("order_title, order_description, order_price, delivery_location",
                         [
                             ("", "order_description",
                                 "order_price", "delivery_location"),
                             ("order_title", "", "order_price",
                                 "delivery_location"),
                             ("order_title", "order_description",
                                 "", "delivery_location"),
                             ("order_title", "order_description",
                                 "order_price", ""),
                         ])
def test_submit_with_empty_value(order_title, order_description, order_price, delivery_location):
    response = app.test_client().post('/api/v1/orders', data=json.dumps(dict(
        order_title=order_title, order_description=order_description,
        order_price=order_price, delivery_location=delivery_location)), content_type='application/json')
    message = json.loads(response.get_data(as_text=True))[
        "message"]
    if not order_title:
        assert message == "either order_title is not set or empty"
    if not order_description:
        assert message == "either order_description is not set or empty"
    if not order_price:
        assert message == "either order_price is not set or empty"
    if not delivery_location:
        assert message == "either delivery_location is not set or empty"


def test_submit_with_full_value():
    response = app.test_client().post('/api/v1/orders', data=json.dumps(dict(
        order_title="order_title", order_description="order_description",
        order_price="order_price", delivery_location="delivery_location")), content_type='application/json')
    assert response.status_code == 200
