from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, MessageResponse
from app.api.v1.customer_orders import customer_orders
from flask_jwt_extended import (
    create_access_token,
    verify_fresh_jwt_in_request,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt)

api_update_order_status = Blueprint('update_order_status', __name__)


@api_update_order_status.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
@jwt_required
def update_order_status(order_id):
    """updates order status"""
    current_user = get_jwt_identity()
    if current_user["user_type"] == 'admin':
        if request.method == "PUT":
            data = request.get_json()
            if not data.get('order_status'):
                return MessageResponse.send("either order_status is not set or empty", 406)

            order_status = data.get('order_status')
            status = customer_orders.change_status(order_id, order_status)
            if status == "order does not exist":
                return MessageResponse.send(status, 404)
            else:
                return MessageResponse.send(status, 200)
    else:
        return MessageResponse().send("You need to be an admin to access this route", 406)
