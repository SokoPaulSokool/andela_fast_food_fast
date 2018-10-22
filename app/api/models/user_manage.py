from app.api.models.database.crud_users_table import QueryUsersTable
from flask import Blueprint, request, jsonify, json
from app.api.models.message_response import MessageResponse
from passlib.hash import pbkdf2_sha256 as sha256
import datetime
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt)


class User:
    """creates order"""

    def __init__(self, user_id, user_name, email, password, user_type):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.password = sha256.hash(password)
        self.user_type = user_type

    def toJSON(self):
        return {"user_id": self.user_id, "user_name": self.user_name,
                "email": self.email, "password": self.password,
                "user_type": self.user_type
                }

    @staticmethod
    def authenticate_user(email, password):
        """Authenticate user
        """
        check_result = QueryUsersTable().get_user_by_email(email)
        print(check_result[1])
        if check_result == 'failed':
            return MessageResponse().send(
                "Login failed  email does not exist. First signup",
                401)
        else:
            if sha256.verify(password, check_result[3]):
                access_token = create_access_token(
                    identity={
                        "user_id": check_result[0],
                        "user_name": check_result[1],
                        "user_type": check_result[4]},
                        expires_delta= datetime.timedelta(minutes=30)
                        )
                message = check_result[1] + \
                    " has been authorised."
                return jsonify({
                    "message": message,
                    'access_token': access_token,
                    "account_type": check_result[4]
                }), 200
            else:
                return MessageResponse.send(
                    "login failed  wrong password ", 401)
