import allure
import pytest


from api_methods.api_user import User
from data import Credentials

@allure.epic('Тестирование сервиса Stellar burger')
@allure.feature('Авторизация пользователя')
class TestLoginUser:

    @allure.story('Успешная авторизация пользователя')
    @allure.title('Вход под существующим пользователем')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_existing_user_can_login(self, create_delete_user):
        response = User.login_user(create_delete_user)

        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "accessToken" in response.json()

    @allure.story('Ошибка авторизации пользователя')
    @allure.title('Вход c неверным {field} пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('field, data', [
                                            ["email", Credentials.email], 
                                            ["password", Credentials.password]
                                        
                                        ])
    def test_login_with_invalid_parametrize(self, create_delete_user, field, data):
        payload = create_delete_user
        payload[field] = data
        response = User.login_user(payload)

        assert response.status_code == 401
        assert response.json()["success"] == False
        assert response.json()["message"] == "email or password are incorrect"