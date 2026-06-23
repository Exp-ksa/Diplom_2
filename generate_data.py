from faker import Faker
import random

faker = Faker('ru_RU')

def generate_user_data():
    # Генерируем имя
    name = faker.first_name()

    # Генерируем email
    digits = f"{random.randint(0, 9999):04d}"  # Всегда 3 цифры с ведущими нулями
    email = f"sergey_kuznetsov_45_{digits}@yandex.ru"
    
    # Пароль 
    password = faker.password(length=6, special_chars=True, digits=True)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    
    return payload

def generate_hesh_data():
    # Генерируем рандомный хэш длиной с оригинальный
    invalid_hash = ''.join(random.choices('abcdef0123456789', k=24))
    return f'"{invalid_hash}"'