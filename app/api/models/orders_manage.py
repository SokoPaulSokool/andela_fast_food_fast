import datetime
from app.api.models.database.crud_orders_table import QueryOrdersTable


class Menu:
    """creates order"""

    def __init__(self, item_id, item_name, item_description, item_price):
        self.item_id = item_id
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price

    def toJSON(self):
        return {"item_id": self.item_id, "item_name": self.item_name,
                "item_description": self.item_description, "item_price": self.item_price
                }


class OrderItem:
    """creates order"""

    def __init__(self, order_id, user_id, item_id, delivery_location):
        self.order_id = order_id
        self.user_id = user_id
        self.item_id = item_id
        self.delivery_location = delivery_location
        self.created_at = datetime.datetime.now()
        self.edited_at = datetime.datetime.now()
        self.order_status = "incomplete"

    def toJSON(self):
        return {"order_id": self.order_id, "user_id": self.user_id,
                "item_id": self.item_id, "delivery_location": self.delivery_location,
                "created_at": self.created_at, "edited_at": self.edited_at,
                "order_status": self.order_status
                }

    @staticmethod
    def fromTurple(order_item_turple):
        order = OrderItem(
            order_item_turple[0], order_item_turple[1], order_item_turple[2], order_item_turple[4])
        order.order_status = order_item_turple[3]
        order.created_at = order_item_turple[5]
        order.edited_at = order_item_turple[6]
        return order


class Order:
    """creates order"""

    def __init__(self, order_title, order_description, order_price, delivery_location):
        self.order_title = order_title
        self.order_description = order_description
        self.order_price = order_price
        self.delivery_location = delivery_location
        self.created_at = datetime.datetime.now().timestamp()
        self.order_status = "incomplete"
        self.order_id = ''

    def toJSON(self):
        return {"order_id": self.order_id, "order_title": self.order_title,
                "order_description": self.order_description, "order_price": self.order_price,
                "delivery_location": self.delivery_location, "created_at": self.created_at,
                "order_status": self.order_status
                }


class CustomerOrders:
    def __init__(self):
        self.orders_list = []

    def place_order(self, new_order: OrderItem):
        """assigns id to new order and adds it to orders list"""
        order_result = QueryOrdersTable().add_order(new_order)
        if order_result == "failed":
            return "item does not exist on menu"
        else:
            print(order_result)
            item = OrderItem.fromTurple(order_result)
            return item.toJSON()

    def get_all_orders(self):
        """returns all orders in the list"""
        orders = QueryOrdersTable().get_all_orders()
        new_list = []
        for key in range(len(orders)):
            new_list.append(OrderItem.fromTurple(orders[key]))
        return new_list

    def get_orders_for_specific_user(self, user_id):
        """returns all users orders orders in the list"""
        orders = QueryOrdersTable().get_all_orders_for_user(user_id)
        new_list = []
        for key in range(len(orders)):
            new_list.append(OrderItem.fromTurple(orders[key]))
        return new_list

    def is_order_exist(self, id):
        """checks if order exists in the list"""
        order_result = QueryOrdersTable().get_order_by_id(id)
        if order_result == "failed":
            return False
        else:
            return True

    def get_order(self, id):
        """gets order by id if it exists"""

        order_result = QueryOrdersTable().get_order_by_id(id)
        if order_result == "failed":
            return "order does not exist"
        else:
            return OrderItem.fromTurple(order_result)

    def delete_order(self, id):
        """deletes order by id if it exists"""
        order_result = QueryOrdersTable().get_order_by_id(id)

        order_result = QueryOrdersTable().delete_order_by_id(id)
        if order_result == "failed":
            return "order does not exist"
        elif order_result > 0:
            return "deleted"
        else:
            return "order does not exist"

    def change_status(self, id, status):
        """changes order status by id if it exists"""

        order_result = QueryOrdersTable().update_order_status(id, status)
        if not self.is_order_exist(id):
            return "order does not exist"
        else:
            print(order_result)
            order = OrderItem.fromTurple(order_result)
            return "status changed to "+order.order_status
