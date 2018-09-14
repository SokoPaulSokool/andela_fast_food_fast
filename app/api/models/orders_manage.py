import datetime


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

    def place_order(self, new_order: Order):
        """assigns id to new order and adds it to orders list"""

        if len(self.orders_list) >= 0:
            new_order.order_id = len(self.orders_list)
        else:
            new_order.order_id = 0
        self.orders_list.append(new_order)

    def get_all_orders(self):
        """returns all orders in the list"""

        return self.orders_list

    def is_order_exist(self, id):
        """checks if order exists in the list"""

        if len(self.orders_list) > id and id >= 0:
            return True
        else:
            return False

    def get_order(self, id):
        """gets order by id if it exists"""

        if self.is_order_exist(id):
            return self.orders_list[id]
        else:
            return "order does not exist"

    def delete_order(self, id):
        """deletes order by id if it exists"""

        if self.is_order_exist(id):
            self.orders_list.pop(id)
            return "deleted"
        else:
            return "order does not exist"

    def change_status(self, id, status):
        """changes order status by id if it exists"""

        if self.is_order_exist(id):
            self.orders_list[id].order_status = status
            return "status changed to "+status
        else:
            return "order does not exist"
