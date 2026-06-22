import random
import re
import string
from faker import Faker


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def generate_courier_random():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
 
    return payload

def generate_fake_id_courier():
    courier_id = random.randint(100000000, 999999999)
    return courier_id

def generate_fake_id_order():
    order_id = random.randint(100000000, 999999999)
    return order_id

faker = Faker('ru_RU')

def generate_order():
    
    first_name = faker.first_name()
    last_name = faker.last_name()
    address = re.sub(r'[^а-яА-ЯёЁa-zA-Z0-9., ]', '',faker.address()[:30])
    station = random.randint(1, 237)
    phone = f"+{random.randint(00000000000, 99999999999)}"
    date = faker.date_between(start_date='+1d', end_date='+15d').isoformat()
    rental = random.randint(1, 7)
    color = random.choice([["BLACK"], ["GREY"], [], ["BLACK", "GREY"]])
    comments_courier = faker.text(max_nb_chars=100)
    
    test = {
    "firstName": f"{first_name}",
    "lastName": f"{last_name}",
    "address": f"{address}",
    "metroStation": station,
    "phone": f"{phone}",
    "rentTime": rental,
    "deliveryDate": f"{date}",
    "comment": f"{comments_courier}",
    "color": color
    }
    return test