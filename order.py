from customer import Customer
from coffee import Coffee
class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee.")
        if not isinstance(price, (int, float)) or price < 1.0 or price >10.0:
            raise ValueError("Price must be a positive number.")
        
        self._customer = customer
        self._coffee = coffee
        self._price = int(price)

        coffee._orders.append(self)
        customer._orders.append(self)

    @property
    def price(self):
        return self._price
    
    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee
    

    
    
