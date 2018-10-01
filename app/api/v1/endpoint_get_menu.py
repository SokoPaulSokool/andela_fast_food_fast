from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders
from app.api.v1.customer_orders import customer_orders

api_get_menu = Blueprint('get_menu', __name__)

menu = [
    {
        'menu_title': 'FRIED CHICKEN',
        'price': '40,000 UGX',
        'id':1
    },
    {
        'menu_title': 'FRENCH FRIES',
        'price': '50,000 UGX',
        'id':2
    },
    {
        'menu_title': 'HUMBURGER',
        'price': '9000 UGX',
        'id':3
    }
]


@api_get_menu.route('/api/v1/menu', methods=['GET'])
def get_menu():
    """gets menu"""
    if request.method == "GET":
        return jsonify(menu), 200