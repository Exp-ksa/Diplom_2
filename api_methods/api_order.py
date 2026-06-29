import allure
import requests

from url import Url

class Order:

    @staticmethod
    @allure.step('Получение данных об ингридиентах')
    def get_ingredients():
        return requests.get(Url.GET_INGREDIENTS_ENDPOINT, verify=False)

    @staticmethod
    @allure.step('Создание заказа с игридиентами: {payload}')
    def create_order(payload, token=None):
        headers = {"Authorization": token} if token else {}
        return requests.post(Url.ORDER_ENDPOINT, headers=headers, json=payload, verify=False)   

    @staticmethod
    @allure.step('Получение заказов пользователя')
    def get_order_user(token):
        return requests.get(Url.ORDER_ENDPOINT, headers={"Authorization": token}, verify=False)
    
    @staticmethod
    @allure.step('Получение всех заказов')
    def get_all_order():
        return requests.get(Url.GET_ALL_ORDER_ENDPOINT, verify=False)
 