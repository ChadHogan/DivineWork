from faker import Faker
import json

fake = Faker()

def generate_mock_orders(num_orders):
    orders = []
    for _ in range(num_orders):
        order = {
            'order_number': fake.unique.random_number(digits=5),
            'order_date': fake.date_between(start_date='-30d', end_date='today'),
            'items': generate_mock_items(fake.random_int(min=1, max=3))
        }
        orders.append(order)
    return orders


def generate_mock_items(num_items):
    items = []
    price_item_tuple = [
    (2.90, "latte"),
    (3.00, "mocha"),
    (3.10, "cappuccino")
]
    for _ in range(num_items):
        price, coffee = fake.random_element(elements=price_item_tuple)
        item = {
            'item_name': coffee.capitalize(),
            'quantity': fake.random_int(min=1, max = 3),
            'price': price,
            'total': 0
        }
        item['total'] = item['quantity'] * item['price']
        items.append(item)
    return items

mock_orders = generate_mock_orders(10)

with open('/Users/Emma/Desktop/DataStuff/EposWork/EShop_data.json', 'w') as file:
    json.dump(mock_orders, file, default=str)

print(mock_orders)