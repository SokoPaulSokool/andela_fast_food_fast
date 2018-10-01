import psycopg2
from database.connection import connect
from database.create_tables import create_tables
import psycopg2.extras as extra
from app.api.models.user_manage import User


class auth_crud():
    def __init__(self):
        self.conn = connect()
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(
            cursor_factory=extra.DictCursor)

    def add_user(self, user: User):
        """Add user to database"""

        try:
            if self.get_user_by_email(user.email) == 'failed':
                cur = self.conn.cursor()
                db_query = """INSERT INTO Users (user_id, user_name , email, password, user_type)
                            VALUES (DEFAULT,%s,%s,%s) RETURNING user_id, name, email, password, user_type """
                cur.execute(db_query, (user.user_name, user.email,
                                       user.password, user.user_type))

                print("created")
                rows = cur.fetchone()
                return rows
            else:
                return 'user exists'

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return 'failed'

    def get_user_by_email(self, email):
        """Get user by email"""

        cur = self.conn.cursor()
        try:
            cur.execute(
                """SELECT * from Users WHERE email = %s  """,
                [email])
            rows = cur.fetchall()
            return rows[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"

    def delete_user_by_email(self, email):
        """Delete user by email"""

        cur = self.conn.cursor()
        try:
            cur.execute(
                """DELETE FROM  Users WHERE email = %s  """,
                [email])
            rows = cur.fetchall()
            return rows[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "failed"
