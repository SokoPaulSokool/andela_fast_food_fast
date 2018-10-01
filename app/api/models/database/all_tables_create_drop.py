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
                """CREATE TABLE IF NOT EXISTS  "Users"(
                user_id SERIAL PRIMARY KEY, 
                user_name VARCHAR(20),
                email VARCHAR(20),
                password VARCHAR(260),
                user_type VARCHAR(20)
                )
                """)
            self.cursor.execute(create_table_query)
            self.conn.commit()
            print("creating Users table")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
