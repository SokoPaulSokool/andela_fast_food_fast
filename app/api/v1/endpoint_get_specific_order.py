from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, MessageResponse
from app.api.v1.customer_orders import customer_orders
from app.api.models.user_manage import User
from flasgger import swag_from
from flask_jwt_extended import (
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt)

api_get_specific_order = Blueprint('get_specific_order', __name__)


@api_get_specific_order.route('/api/v1/orders/<int:order_id>', methods=['GET'])
@jwt_required
@swag_from('../../docs/orders/admin_get_specific_orders.yaml')
def get_specific_order(order_id):
    """gets user order by id"""
    current_user = get_jwt_identity()
    if current_user["user_type"] == 'admin':
        if request.method == "GET":
            the_order = customer_orders.get_order(order_id)
            if the_order == "order does not exist":
                return MessageResponse.send(the_order, 404)
            else:
                return jsonify(the_order), 200

    else:
        return MessageResponse().send("You need to be an admin to access this route", 406)
