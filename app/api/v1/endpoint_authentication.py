from flask import Blueprint, request, jsonify, json
from app.api.models import MessageResponse
from app.api.models.user_manage import User
from app.api.models.database.crud_users_table import QueryUsersTable
from re import match

api_signup = Blueprint('signup', __name__)


@api_signup.route('/api/v1/auth/signup', methods=['POST'])
def signup():
    """signs up user"""
    if request.method == 'POST':
        data = request.get_json()
        if not data.get('user_name'):
            return MessageResponse.send("either user_name is not set or empty", 406)
        if not data.get('email'):
            return MessageResponse.send("either email is not set or empty", 406)
        if not data.get('password'):
            return MessageResponse.send("either password is not set or empty", 406)
        if not data.get('user_type'):
            return MessageResponse.send("either user_type is not set or empty", 406)

        user_name = data.get('user_name')
        email = data.get('email')
        password = data.get('password')
        user_type = data.get('user_type')

        if not bool(
            match(
                r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",
                email)):
            print(email.isdigit())
            return MessageResponse().send(
                "email is not valid. use example soko@andela.com",
                400)
        if len(password) < 5:
            return ResponseMessage().send(
                "password is too short. mut have atleats 5 characters",
                400)

        new_user = User("", user_name, email, password, user_type)

        result = QueryUsersTable().add_user(new_user)
        return MessageResponse.send(result, 200)


api_login = Blueprint('login', __name__)


@api_signup.route('/api/v1/auth/login', methods=['POST'])
def login():
    """Logs in up user"""
    if request.method == 'POST':
        data = request.get_json()
        if not data.get('email'):
            return MessageResponse.send("either email is not set or empty", 406)
        if not data.get('password'):
            return MessageResponse.send("either password is not set or empty", 406)

        email = data.get('email')
        password = data.get('password')
        result = User.authenticate_user(email, password)
        print(result)
        return result
