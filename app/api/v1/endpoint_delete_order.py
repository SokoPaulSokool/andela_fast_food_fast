from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, MessageResponse
from app.api.v1.customer_orders import customer_orders

api_delete_order = Blueprint('delete_order', __name__)


@api_delete_order.route('/api/v1/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """deletes order"""
    if request.method == "DELETE":
        the_order = customer_orders.delete_order(order_id)
        if the_order == "order does not exist":
            return MessageResponse.send(the_order, 404)
        else:
            return MessageResponse.send(the_order, 200)
