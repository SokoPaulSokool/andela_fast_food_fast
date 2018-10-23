from app import app
from flask import redirect
from app.api.models.database.all_tables_create_drop import create_tables
from app.api.models.user_manage import User
from app.api.models.database.crud_users_table import QueryUsersTable


if __name__ == '__main__':
    create_tables().users_drop_table()
    create_tables().menu_drop_table()
    create_tables().orders_drop_table()
    create_tables().users_table()
    create_tables().menu_table()
    create_tables().orders_table()

    new_user = User("", "soko", "soko@gmail.com", "pass1234", "admin")

    QueryUsersTable().add_user(new_user)
    app.run(debug=True)
