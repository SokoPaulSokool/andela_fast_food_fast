from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, MessageResponse
from app.api.v1.customer_orders import customer_orders
from flasgger import swag_from

from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.orders_manage import Menu

from flask_jwt_extended import (
    create_access_token,
    verify_fresh_jwt_in_request,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt)

api_delete_menu = Blueprint('delete_menu', __name__)


@api_delete_menu.route('/api/v1/menu/<int:order_id>', methods=['DELETE'])
@jwt_required
@swag_from('../../docs/menu/delete_menu.yaml')
def delete_menu(order_id):
    """updates update menu"""
    current_user = get_jwt_identity()
    if current_user["user_type"] == 'admin':
        if request.method == "DELETE":
            result = QueryMenuTable().delete_item_by_id(order_id)
            print(result)
            if result == "failed":
                return MessageResponse.send(result, 404)
            elif result == 0:
                return MessageResponse.send("Item does not exist", 404)
            else:
                return MessageResponse.send("deleted", 200)
    else:
        return MessageResponse().send("You need to be an admin to access this route", 406)
