from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders
from app.api.v1.customer_orders import customer_orders
from app.api.models.database.crud_orders_table import QueryOrdersTable
from app.api.models.orders_manage import OrderItem

api_get_all_orders = Blueprint('get_all_orders', __name__)


@api_get_all_orders.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    """gets all user orders"""
    if request.method == "GET":
        all_orders = []
        for key in range(len(customer_orders.get_all_orders())):
            all_orders.append(customer_orders.get_all_orders()[key].toJSON())

        return jsonify(all_orders), 200
