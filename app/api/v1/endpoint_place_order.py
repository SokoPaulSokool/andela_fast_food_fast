from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, MessageResponse, OrderItem
from app.api.v1.customer_orders import customer_orders
from flask_jwt_extended import (
    create_access_token,
    verify_fresh_jwt_in_request,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt)

api_place_order = Blueprint('place_order', __name__)


@api_place_order.route('/api/v1/users/orders', methods=['POST'])
@jwt_required
def place_order():
    """adds order all to orders list"""
    current_user = get_jwt_identity()
    if current_user["user_id"]:
        user_id = current_user["user_id"]
        print(user_id)
        if request.method == 'POST':
            data = request.get_json()
            if not data.get('item_id'):
                return MessageResponse.send("either item_id is not set or empty", 406)
            if not data.get('delivery_location'):
                return MessageResponse.send("either delivery_location is not set or empty", 406)

            item_id = data.get('item_id')
            delivery_location = data.get('delivery_location')

            new_order = OrderItem("", user_id, item_id, delivery_location)

            result = customer_orders.place_order(new_order)
            return MessageResponse.send(result, 200)
