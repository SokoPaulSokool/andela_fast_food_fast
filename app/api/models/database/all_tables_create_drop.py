import psycopg2
from app.api.models.database.connection import connect
import psycopg2.extras as extra
import os


class create_tables():
    def __init__(self):
        self.conn = connect()
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(
            cursor_factory=extra.DictCursor)

    def users_table(self):
        """Create users table"""

        try:
            create_table_query = (
                """CREATE TABLE IF NOT EXISTS  Users(
                user_id SERIAL PRIMARY KEY, 
                user_name VARCHAR(20),
                email VARCHAR(20),
                password VARCHAR(260),
                user_type VARCHAR(20)
                )
                """)
            self.cursor.execute(create_table_query)
            print("creating Users table")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def menu_table(self):
        """Create menu table"""
        self.conn
        try:
            create_table_query = (
                """CREATE TABLE IF NOT EXISTS Menu (
                        item_id SERIAL PRIMARY KEY,
                        item_name VARCHAR(255) NOT NULL,
                        item_description VARCHAR(255) NOT NULL, 
                        item_price VARCHAR(255) NOT NULL
                        )
                        """)
            self.cursor.execute(create_table_query)
            print("creating Menu table")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def orders_table(self):
        """Create orders table"""
        self.conn
        try:
            create_table_query = (
                """CREATE TABLE IF NOT EXISTS Orders (
                        order_id SERIAL PRIMARY KEY,
                        user_id INTEGER,
                        item_id INTEGER,
                        delivery_location VARCHAR(255) NOT NULL, 
                        created_at VARCHAR(255) NOT NULL,
                        edited_at VARCHAR(255) NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES Users (user_id) ON DELETE CASCADE,
                        FOREIGN KEY (item_id) REFERENCES Menu (item_id) ON DELETE CASCADE
                        )
                        """)
            self.cursor.execute(create_table_query)
            print("creating Orders table")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def users_drop_table(self):
        """Drop Users table"""

        self.conn
        try:
            self.cursor.execute(
                """DROP TABLE IF EXISTS Users CASCADE;""")
            print("Dropping Users table")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def menu_drop_table(self):
        "Drop Menu table"
        try:
            self.conn
            self.cursor.execute("""DROP TABLE Menu CASCADE;""")
            print("Dropping Menu table")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def orders_drop_table(self):
        "Drop Orders table"
        try:
            self.conn
            self.cursor.execute("""DROP TABLE Orders CASCADE;""")
            print("Dropping Orders table")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
