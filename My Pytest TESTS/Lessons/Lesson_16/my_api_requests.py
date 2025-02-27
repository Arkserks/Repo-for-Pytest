from http.client import responses

import requests


def auth_identificate(): # Отправка СМС-кода
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


def auth_login_v2(): # Получение токена
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
    return response.json().get('response', {}).get('token')


def drivers_list():  # Получение списка всех водителей компании
    token = auth_login_v2()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(
        'https://apidev.solber.ru/api/drivers/list',
        headers=headers
    )
    assert response.status_code == 200, response.json()
    print(response.json())


auth_identificate()
drivers_list()
