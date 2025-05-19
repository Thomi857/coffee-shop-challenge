from order import Order
class Customer:
    def __init__(self, name: str):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)#Order
        self._orders.append(order)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        max_spent = -1
        top_customer = None
        for order in coffee.orders():
            if order.customer == cls:
                total_spent = sum(o.price for o in cls.orders())
                if total_spent > max_spent:
                    max_spent = total_spent
                    top_customer = cls
        return top_customer
