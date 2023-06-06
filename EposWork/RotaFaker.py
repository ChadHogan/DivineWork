from faker import Faker
import json

fake = Faker()
staffnames = ['freddy', 'james', 'chris', 'alex', 'jane', 'amy']

def generate_rota():
    staff = []
    for el in staffnames:
        staff_rota = {
            'id': fake.random_number(digits=9),
            'name': el,
            'email': fake.email(),
            'location': 'York',
            'shifts': generate_shifts(4)
        }
        staff.append(staff_rota)
    return staff



def generate_shifts(num_shifts):
    shifts = []
    for _ in range(num_shifts):
        shift_pat = {
            'start_at': fake.date(),
            'end_at': fake.date(),
            'role': fake.random_number(digits=4)
            }
        shifts.append(shift_pat)
    return shifts


narg = generate_rota()


with open('/Users/Emma/Desktop/DataStuff/EposWork/rota_data.json', 'w') as file:
    json.dump(narg, file)

print(narg)