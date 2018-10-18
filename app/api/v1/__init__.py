from flask import Flask, render_template
from app.api.v1.endpoint_get_all_orders import api_get_all_orders, api_get_all_users_orders
from app.api.v1.endpoint_place_order import api_place_order
from app.api.v1.endpoint_get_specific_order import api_get_specific_order
from app.api.v1.endpoint_update_order_status import api_update_order_status
from app.api.v1.endpoint_delete_order import api_delete_order
from app.api.v1.endpoint_get_menu import api_get_menu, api_add_menu
from app.api.v1.endpoint_authentication import api_signup, api_login
from app.api.v1.default import api_default
from app.api.v1.endpoint_delete_menu import api_delete_menu
import os
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

Swagger(app)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

app.register_blueprint(api_get_specific_order)
app.register_blueprint(api_get_all_orders)
app.register_blueprint(api_place_order)
app.register_blueprint(api_update_order_status)
app.register_blueprint(api_delete_order)
app.register_blueprint(api_get_menu)
app.register_blueprint(api_add_menu)
app.register_blueprint(api_signup)
app.register_blueprint(api_login)
app.register_blueprint(api_get_all_users_orders)
app.register_blueprint(api_default)
app.register_blueprint(api_delete_menu)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'sokool-1234567')
