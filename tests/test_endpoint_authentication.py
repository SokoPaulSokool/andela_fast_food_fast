import unittest
from app import Order, CustomerOrders, app
import json
import pytest


class SignUpHelpers():

    def __init__(self, app):
        self.test_client = app.test_client()

    def signup(self, user_name, email, password, account_type):
        response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(dict(
            user_name=user_name, email=email, password=password, account_type=account_type)),
            content_type='application/json')
        return response


@pytest.mark.parametrize("user_name, email, password, account_type",
                         [
                             ("", "sopapaso1@gmail.com", "password", "admin"),
                             ("soko", "", "password", "admin"),
                             ("soko", "sopapaso2@gmail.com", "", "admin"),
                             ("soko", "sopapaso3@gmail.com", "password", "")
                         ])
def test_submit_with_empty_value(user_name, email, password, account_type):
    response = SignUpHelpers(app).signup(
        user_name, email, password, account_type)
    message = json.loads(response.get_data(as_text=True))[
        "message"]
    if not user_name:
        assert message == "either user_name is not set or empty"
    if not email:
        assert message == "either email is not set or empty"
    if not password:
        assert message == "either password is not set or empty"
    if not account_type:
        assert message == "either account_type is not set or empty"


def test_submit_with_full_value():
    response = SignUpHelpers(app).signup(
        "soko", "opo@gmail.com", "password", "admin")
    message = json.loads(response.get_data(as_text=True))[
        "user_name"]
    assert response.status_code == 200
