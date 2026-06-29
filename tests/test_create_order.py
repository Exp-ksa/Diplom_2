import allure
import pytest

from api_methods.api_order import Order
from api_methods.api_user import User
from data import bun, main, sauce
from generate_data import generate_hesh_data

@allure.epic('Тестирование сервиса Stellar burger')
@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.story('Успешное создание заказа')
    @allure.title('Создание заказа с авторизацией')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_can_be_created_with_authorization(self, create_delete_user, order_payload):
        response = User.login_user(create_delete_user)
        token = response.json()["accessToken"]

        bun, ingredient_ids = order_payload
        payload = {"ingredients": [bun] + ingredient_ids}

        response = Order.create_order(payload, token)

        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "number" in response.json()["order"]

    @allure.story('Ошибка при создании заказа')
    @allure.title('Создание заказа с авторизацией без ингредиентов')
    def test_order_with_authorization_without_ingredients(self, create_delete_user):
        response = User.login_user(create_delete_user)
        token = response.json()["accessToken"]

        payload = {}
        response = Order.create_order(payload, token)

        assert response.status_code == 400
        assert response.json()["success"] == False
        assert response.json()["message"] == "Ingredient ids must be provided"
    

    @allure.story('Успешное создание заказа')
    @allure.title('Создание заказа без авторизации')
    def test_unauthorized_user_create_order(self, order_payload):
        bun, ingredient_ids = order_payload
        payload = {"ingredients": [bun] + ingredient_ids}
        
        response = Order.create_order(payload)

        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "number" in response.json()["order"]
    

    @allure.story('Успешное создание заказа')
    @allure.title('Заказ можно создать с ингредиентами {ingredient}')
    @pytest.mark.parametrize('ingredient', [bun[0]["_id"], 
                                            main[0]["_id"],
                                            sauce[0]["_id"]]
                                            )
    def test_order_with_ingredients_created(self, ingredient):
        payload = {"ingredients": [ingredient]}
        response = Order.create_order(payload)

        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "number" in response.json()["order"]

    @allure.story('Ошибка при создании заказа')
    @allure.title('Нельзя создать заказ без ингредиентов')
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_without_ingredients_returns_error(self):
        payload = {"ingredients": []}
        response = Order.create_order(payload)

        assert response.status_code == 400
        assert response.json()["success"] == False
        assert response.json()["message"] == "Ingredient ids must be provided"
    
    @allure.story('Создание заказа с неверным хешем')
    @allure.title('Нельзя создать заказ с неверным хешем ингредиентов')
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_with_invalid_ingredient_hash_returns_error(self):
        hesh = generate_hesh_data()
        payload = {"ingredients": [hesh]}
        response = Order.create_order(payload)

        assert response.status_code == 500


    @allure.story('Создание заказа с неверным хешем')
    @allure.title('Нельзя создать заказ с неверным хешем ингредиентов с авторизацией')
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_with_invalid_ingredient_hash_returns_error_with_authorization(self, create_delete_user):
        hesh = generate_hesh_data()
        payload = {"ingredients": [hesh]}
        response = User.login_user(create_delete_user)
        token = response.json()["accessToken"]

        response = Order.create_order(payload, token)

        assert response.status_code == 500