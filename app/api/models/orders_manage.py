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
        return self.orders_list
