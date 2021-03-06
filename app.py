from app import app
from flask import redirect
from app.api.models.database.all_tables_create_drop import create_tables


if __name__ == '__main__':
    create_tables().users_drop_table()
    create_tables().menu_drop_table()
    create_tables().orders_drop_table()
    create_tables().users_table()
    create_tables().menu_table()
    create_tables().orders_table()
    app.run(debug=True)
