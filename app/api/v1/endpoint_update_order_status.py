from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, MessageResponse
from app.api.v1.customer_orders import customer_orders

api_update_order_status = Blueprint('update_order_status', __name__)


@api_update_order_status.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    """updates order status"""
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
