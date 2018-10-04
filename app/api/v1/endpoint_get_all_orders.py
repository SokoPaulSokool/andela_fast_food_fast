from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders
from app.api.v1.customer_orders import customer_orders
from app.api.models.database.crud_orders_table import QueryOrdersTable
from app.api.models import MessageResponse
from app.api.models.orders_manage import OrderItem
from flasgger import swag_from
from flask_jwt_extended import (
    create_access_token,
    verify_fresh_jwt_in_request,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt)

api_get_all_orders = Blueprint('get_all_orders', __name__)


@api_get_all_orders.route('/api/v1/orders', methods=['GET'])
@jwt_required
@swag_from("../../docs/orders/admin_get_all_orders.yaml")
def get_all_orders():
    """gets all user orders"""
    current_user = get_jwt_identity()
    if current_user["user_type"] == 'admin':
        if request.method == "GET":
            all_orders = []
            for key in range(len(customer_orders.get_all_orders())):
                all_orders.append(
                    customer_orders.get_all_orders()[key])
            return jsonify(all_orders), 200
    else:
        return MessageResponse().send("You need to be an admin to access this route", 406)


api_get_all_users_orders = Blueprint('get_all_users_orders', __name__)


@api_get_all_orders.route('/api/v1/users/orders', methods=['GET'])
@jwt_required
@swag_from("../../docs/orders/get_user_orders.yaml")
def get_all_users_orders():
    """gets all user orders"""
    current_user = get_jwt_identity()
    if current_user["user_id"]:
        user_id = current_user["user_id"]
        if request.method == "GET":
            all_orders = []
            user_orders = customer_orders.get_orders_for_specific_user(user_id)
            for key in range(len(user_orders)):
                all_orders.append(user_orders[key])

            return jsonify(all_orders), 200
    else:
        return MessageResponse().send("You need to be an admin to access this route", 406)
