import psycopg2
from database.connection import connect
from database.create_tables import create_tables
import psycopg2.extras as extra
from app.api.models.orders_manage import Menu


class QueryOrdersTable():
    def __init__(self):
        self.conn = connect()
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(
            cursor_factory=extra.DictCursor)

    def add_order(self, order):
        """Add order table"""
        pass

    def get_order_by_id(self, order_id):
        """Get food item  by id"""
        pass

    def get_all_orders(self):
        """Get all orders"""
        pass

    def delete_order_by_id(self, order_id):
        """Delete order by id"""
        pass
