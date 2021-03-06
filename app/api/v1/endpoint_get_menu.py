from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders
from app.api.v1.customer_orders import customer_orders
from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.orders_manage import Menu
from app.api.models.user_manage import User
from app.api.models import Order, CustomerOrders, MessageResponse
from flasgger import swag_from
from flask_jwt_extended import (
    create_access_token,
    verify_fresh_jwt_in_request,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt)

api_get_menu = Blueprint('get_menu', __name__)


@api_get_menu.route('/api/v1/menu', methods=['GET'])
@jwt_required
@swag_from('../../docs/menu/get_menu.yaml')
def get_menu():
    """gets menu"""
    current_user = get_jwt_identity()
    if current_user:
        if request.method == "GET":
            result = QueryMenuTable().get_all_menu_items()
            items = []
            for key in range(len(result)):
                item = result[key]
                items.append({"item_id": item[0], "item_name": item[1],
                              "item_description": item[2], "item_price": item[3]})
            return jsonify(items), 200


api_add_menu = Blueprint('add_menu', __name__)


@api_add_menu.route('/api/v1/menu', methods=['POST'])
@jwt_required
@swag_from('../../docs/menu/add_menu_item.yaml')
def add_menu():
    """adds menu"""
    current_user = get_jwt_identity()
    if current_user["user_type"] == 'admin':
        if request.method == "POST":
            current_user = get_jwt_identity()
            print(current_user)
            data = request.get_json()
            if not data.get('item_name'):
                return MessageResponse.send("either item_name is not set or empty", 406)
            if not data.get('item_description'):
                return MessageResponse.send("either item_description is not set or empty", 406)
            if not data.get('item_price'):
                return MessageResponse.send("either item_price is not set or empty", 406)
            item_price = data.get('item_price')
            item_name = data.get('item_name')
            item_description = data.get('item_description')
            if not isinstance(item_price, (int)):
                return MessageResponse.send("price must must be a nummber", 406)
            menu_item = Menu("", item_name, item_description, item_price)
            result = QueryMenuTable().add_item(menu_item)
            if result == "failed":
                return "failed", 400
            else:
                return jsonify({"item_id": result[0], "item_name": result[1], "item_description": result[2], "item_price": result[3]}), 200

    else:
        return MessageResponse().send("You need to be an admin to access this route", 406)
