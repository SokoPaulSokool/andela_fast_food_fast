from flask import Flask, render_template
from app.api.v1.endpoint_get_all_orders import api_get_all_orders
from app.api.v1.endpoint_place_order import api_place_order
from app.api.v1.endpoint_get_specific_order import api_get_specific_order
from app.api.v1.endpoint_update_order_status import api_update_order_status
from app.api.v1.endpoint_delete_order import api_delete_order
from app.api.v1.endpoint_get_menu import api_get_menu
import os

app = Flask(__name__)

app.register_blueprint(api_get_specific_order)
app.register_blueprint(api_get_all_orders)
app.register_blueprint(api_place_order)
app.register_blueprint(api_update_order_status)
app.register_blueprint(api_delete_order)
app.register_blueprint(api_get_menu)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'sokool-1234567')
