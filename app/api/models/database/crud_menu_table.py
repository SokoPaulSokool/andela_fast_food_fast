import psycopg2
from app.api.models.database.connection import connect
import psycopg2.extras as extra


class QueryMenuTable():
    def __init__(self):
        self.conn = connect()
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(
            cursor_factory=extra.DictCursor)

    def add_item(self, menu_item):
        """Add item to menu table"""

        try:
            cur = self.conn.cursor()
            db_query = """INSERT INTO Menu (item_id, item_name , item_description, item_price)
                        VALUES (DEFAULT,%s,%s,%s) RETURNING item_id, item_name, item_description, item_price"""
            cur.execute(db_query, (menu_item.item_name, menu_item.item_description,
                                   menu_item.item_price))

            print("created")
            rows = cur.fetchone()
            return rows

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return 'failed'

    def get_item_by_id(self, item_id):
        """Get food item  by id"""

        cur = self.conn.cursor()
        try:
            cur.execute(
                """SELECT * from Menu WHERE item_id = %s  """,
                [item_id])
            rows = cur.fetchall()
            return rows[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"

    def get_all_menu_items(self):
        """Get all food items on menu"""

        cur = self.conn.cursor()
        try:
            cur.execute(
                """SELECT * from Menu """)
            rows = cur.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"

    def delete_item_by_id(self, item_id):
        """Delete food item by email"""

        cur = self.conn.cursor()
        try:
            cur.execute(
                """DELETE FROM  Menu WHERE item_id = %s  """,
                [item_id])
            rows = cur.rowcount
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"
