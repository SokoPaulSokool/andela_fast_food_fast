from flask import Flask, render_template
from app.api.v1.endpoint_get_all_orders import api_get_all_orders
from app.api.v1.endpoint_place_order import api_place_order
from app.api.v1.endpoint_get_specific_order import api_get_specific_order
from app.api.v1.endpoint_update_order_status import api_update_order_status
from app.api.v1.endpoint_delete_order import api_delete_order

app = Flask(__name__)

app.register_blueprint(api_get_specific_order)
app.register_blueprint(api_get_all_orders)
app.register_blueprint(api_place_order)
app.register_blueprint(api_update_order_status)
app.register_blueprint(api_delete_order)
