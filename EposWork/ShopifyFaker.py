from faker import Faker
import json

fake = Faker('en_GB')

def generate_online_orders(num_orders):
    orders = []
    for _ in range(num_orders):
        cof_items = generate_items(1)
        the_order = {
            'id': fake.random_number(digits=9),
            'created_at': fake.date_between(start_date='-7d', end_date='today'),
            
            'items': cof_items,
            'customer': generate_customer(),
            'total_price': cof_items[0]['total']
    }
        #place here the code to srt out pricing of order
        orders.append(the_order)    
    return orders


def generate_customer():

    customer = {
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'shipping_adress': {
                'address': fake.street_name(),
                'city': fake.city(),
                'country': fake.country(),
                'post_code': fake.postcode()
            }
        
    }
    return customer


def generate_items(num_items):
    items = []
    price_item_tuple = [
    (6.00, "Fortuna"),
    (6.00, "Pato"),
    (6.50, "Decaf"),
    (6.50, 'Columbian'),
    (6.00, 'Darkside')
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

varg = generate_online_orders(100)

with open('/Users/Emma/Desktop/DataStuff/EposWork/the_data.json', 'w') as file:
    json.dump(varg, file, default=str)
print(varg)
'''work on the items.. aka what has been brought '''