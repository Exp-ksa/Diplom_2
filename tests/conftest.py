import random

import pytest
import generate_data

from api_methods.api_user import User
from api_methods.api_order import Order

@pytest.fixture(scope="function")
def random_payload():
    """Генерирует случайные данные пользователя"""
    return generate_data.generate_user_data()

@pytest.fixture(scope="function")
def clear_user(random_payload):     
    """Удаляет пользователя"""
    yield random_payload
    
    del random_payload["name"]

    auth_response = User.login_user(random_payload)
    if auth_response.status_code == 200:
        auth_token = auth_response.json()["accessToken"]
        User.delete_user(auth_token)

@pytest.fixture(scope="function")
def create_delete_user(random_payload):
    """Создаёт пользователя для заказа и удаляет после теста"""
    response = User.create_user(random_payload)
    if response.status_code == 200:
        del random_payload["name"]
    
    yield random_payload
        
    # Удаляем тестовые данные
    auth_response = User.login_user(random_payload)
    if auth_response.status_code == 200:
        auth_token = auth_response.json()["accessToken"]
        User.delete_user(auth_token)

@pytest.fixture(scope="function")
def order_payload():
    """Генерирует случайный набор ингредиентов и возвращает bun и ingredient_ids"""
    response = Order.get_ingredients()
    ingredients = response.json()["data"]
    
    buns = [item for item in ingredients if item["type"] == "bun"]
    sauces = [item for item in ingredients if item["type"] == "sauce"]
    mains = [item for item in ingredients if item["type"] == "main"]
    
    bun = random.choice(buns)["_id"]
    ingredient_count = random.randint(1, 5)
    random_ingredients = random.sample(mains + sauces, ingredient_count)
    ingredient_ids = [item["_id"] for item in random_ingredients]
    
    return bun, ingredient_ids