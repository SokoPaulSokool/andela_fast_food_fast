import psycopg2
from app.api.models.database.connection import connect
import psycopg2.extras as extra
from app.api.models.database.crud_menu_table import QueryMenuTable
from app.api.models.database.crud_users_table import QueryUsersTable
import datetime


class QueryOrdersTable():
    def __init__(self):
        self.conn = connect()
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(
            cursor_factory=extra.DictCursor)

    def add_order(self, order):
        """Add order table"""
        try:
            cur = self.conn.cursor()
            db_query = """INSERT INTO Orders (order_id, user_id , item_id,order_status, delivery_location, created_at, edited_at)
                            VALUES (DEFAULT,%s,%s,%s, %s,%s, %s) RETURNING order_id, user_id, item_id,order_status, delivery_location, created_at, edited_at ;"""
            cur.execute(db_query, (order.user_id, order.item_id, order.order_status,
                                   order.delivery_location, order.created_at, order.edited_at))

            rows = cur.fetchone()

            return rows

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return 'failed'

    def get_order_by_id(self, order_id):
        """Get order item item  by id"""
        cur = self.conn.cursor()
        try:
            cur.execute(
                """SELECT * from Orders WHERE order_id = %s  """,
                [order_id])
            rows = cur.fetchall()
            return rows[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"

    def get_all_orders(self):
        """Get all orders"""
        cur = self.conn.cursor()
        try:
            cur.execute(
                """SELECT * from Orders""")
            rows = cur.fetchall()

            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"

    def get_all_orders_for_user(self, user_id):
        """Get all orders for specific user"""
        cur = self.conn.cursor()
        try:
            cur.execute(
                """SELECT * from Orders WHERE user_id = %s  """,
                [user_id])
            rows = cur.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"

    def delete_order_by_id(self, order_id):
        """Delete order by id"""
        cur = self.conn.cursor()
        try:
            cur.execute(
                """DELETE from Orders WHERE order_id = %s ; """,
                [order_id])
            rows = cur.rowcount
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"

    def update_order_status(self, order_id, order_status):
        """Update  order by id"""
        cur = self.conn.cursor()
        try:
            edited_at = datetime.datetime.now().timestamp()
            cur.execute(
                """UPDATE Orders SET order_status =  %s, edited_at =  %s
             WHERE order_id = %s  RETURNING order_id, user_id, item_id,order_status, delivery_location, created_at, edited_at ;""",
                (order_status, edited_at, order_id))
            rows = cur.fetchone()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"
