import allure

from api_methods.api_user import User


@allure.epic('Тестирование сервиса Stellar burger')
@allure.feature('Создание пользователя')
class TestCreateUser:

    @allure.story('Успешное создание пользователя')
    @allure.title('Пользователя можно создать')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_be_created(self, clear_user):
        
        response = User.create_user(clear_user)
        
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()["user"]["email"] == clear_user["email"]

    @allure.story('Ошибки при создании пользователя')
    @allure.title('Нельзя создать пользователя, который уже зарегистрирован')
    @allure.severity(allure.severity_level.NORMAL)
    def test_duplicate_user_cannot_be_created(self, clear_user):
        
        response = User.create_user(clear_user)
        assert response.status_code == 200

        response = User.create_user(clear_user)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.story('Ошибки при создании пользователя')
    @allure.title('Если нет email, запрос возвращает ошибку')
    def test_create_user_missing_field_email_returns_error(self, random_payload):
        del random_payload["email"]
        response = User.create_user(random_payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.story('Ошибки при создании пользователя')
    @allure.title('Если нет password, запрос возвращает ошибку')
    def test_create_user_missing_field_password_returns_error(self, random_payload):
        del random_payload["password"]
        response = User.create_user(random_payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.story('Ошибки при создании пользователя')
    @allure.title('Если нет name, запрос возвращает ошибку')
    def test_create_user_missing_field_name_returns_error(self, random_payload):
        del random_payload["name"]
        response = User.create_user(random_payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"