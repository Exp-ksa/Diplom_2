class Url:
    BASE_URL = "https://stellarburgers.education-services.ru"
    GET_INGREDIENTS_ENDPOINT = f"{BASE_URL}/api/ingredients"
    ORDER_ENDPOINT = f"{BASE_URL}/api/orders"
    CREATE_USER_ENDPOINT = f"{BASE_URL}/api/auth/register"
    AUTHORIZATION_ENDPOINT = f"{BASE_URL}/api/auth/login"
    LOGOUT_USER_ENDPOINT = f"{BASE_URL}/api/auth/logout"
    GET_TOKEN_ENDPOINT = f"{BASE_URL}/api/auth/token"
    USER_DATA_ENDPOINT = f"{BASE_URL}/api/auth/user"
    GET_ALL_ORDER_ENDPOINT = f"{BASE_URL}/api/orders/all"

