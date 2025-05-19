from order import Order
from coffee import Coffee
from customer import Customer

# Create instances
customer = Customer("Alice")
coffee = Coffee("Latte")

# Link via Order
order1 = Order(customer, coffee, 5.5)
order2 = Order(customer, coffee, 6.0)

# Test relationships
print(customer.orders())   # [order1, order2]
print(customer.coffees())  # [Latte] (unique)
print(coffee.orders())     # [order1, order2]
print(coffee.customers())  # [Alice] (unique)
print(coffee.average_price())  # 5.75