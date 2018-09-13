from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, MessageResponse
from app.api.v1.customer_orders import customer_orders

api_place_order = Blueprint('place_order', __name__)


@api_place_order.route('/api/v1/orders', methods=['POST'])
def place_order():
    """adds order all to orders list"""
    if request.method == 'POST':
        data = request.get_json()
        if not data.get('order_title'):
            return MessageResponse.send("either order_title is not set or empty", 406)
        if not data.get('order_description'):
            return MessageResponse.send("either order_description is not set or empty", 406)
        if not data.get('order_price'):
            return MessageResponse.send("either order_price is not set or empty", 406)
        if not data.get('delivery_location'):
            return MessageResponse.send("either delivery_location is not set or empty", 406)

        order_title = data.get('order_title')
        order_description = data.get('order_description')
        order_price = data.get('order_price')
        delivery_location = data.get('delivery_location')

        new_order = Order(order_title, order_description,
                          order_price, delivery_location)

        customer_orders.place_order(new_order)
        return MessageResponse.send("order for "+order_title+" successfully placed", 200)
