import requests
import pytest



@pytest.fixture()
def auth_portal():
    def send_sms(): # Отправка СМС-кода (auth_identificate)
        body = {
            "phone": "+79000000001"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://apidev.solber.ru/api/auth/identificate',
            json=body,
            headers=headers
        )
        assert response.status_code == 204, response.json()

    def get_auth_token(): # Получение токена (auth_login_v2)
        body = {
            "phone": "+79000000001",
            "code": 42429
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://apidev.solber.ru/api/auth/login/v2',
            json=body,
            headers=headers
        )
        assert response.status_code == 200, response.json()
        auth_token = response.json().get('response', {}).get('token')
        return auth_token

        # Вызов функций и возврат токена
    send_sms()
    token = get_auth_token()
    return token


# Параметризация теста
@pytest.mark.parametrize("endpoint, expected_status", [
    ("/api/drivers/list", 200),  # Первый набор данных
    ("/api/drivers/invalid", 404),  # Второй набор данных
])
@pytest.mark.smoke
def test_drivers_list(auth_portal, endpoint, expected_status):  # Получение списка всех водителей компании
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_portal}'
    }
    response = requests.get(
        'https://apidev.solber.ru/api/drivers/list',
        headers=headers
    )
    assert response.status_code == expected_status, response.json()
    print(response.json())
