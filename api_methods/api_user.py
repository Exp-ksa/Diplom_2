import allure
import requests

from url import Url

class User:

    @staticmethod
    @allure.step('Создание пользователя с данными: {payload}')
    def create_user(payload):
        return requests.post(Url.CREATE_USER_ENDPOINT, data=payload, verify=False)

    @staticmethod
    @allure.step('Авторизация пользователя с данными: {payload}')
    def login_user(payload):
        return requests.post(Url.AUTHORIZATION_ENDPOINT, data=payload, verify=False)   

    @staticmethod
    @allure.step('Выход из системы пользователя с данными: {payload}')
    def logout_user(payload):
        return requests.post(Url.LOGOUT_USER_ENDPOINT, data=payload, verify=False)
    
    @staticmethod
    @allure.step('Получение данных пользователя')
    def get_user_data(token):
        return requests.get(Url.USER_DATA_ENDPOINT, headers={"Authorization": token}, verify=False)

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        return requests.delete(Url.USER_DATA_ENDPOINT, headers={"Authorization": token}, verify=False) 