from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders
from app.api.v1.customer_orders import customer_orders

api_get_all_orders = Blueprint('get_all_orders', __name__)


@api_get_all_orders.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    """gets all user orders"""
    return jsonify(customer_orders.get_all_orders()), 200
