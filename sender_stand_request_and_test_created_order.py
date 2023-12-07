import requests
import configuration
import data

# создание нового заказа
def post_create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER,
                         json=body,
                         headers=data.headers)

response = post_create_new_order(data.new_order_body)
# print(response.status_code) ## проверка, что возвращается код 201
# print(response.json()) ## проверка тела ответа
data.t = (response.json()) # сохранение номера трека заказа


# запрос на получение информации о заказе
def get_created_order(data):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={"t": data.t["track"]}) # передача номера трека заказа

order_status = get_created_order(data) # сохранение кода ответа
# print(order_status.status_code) ## проверка, что возвращается код 200
# print(order_status.json()) ## проверка тела ответа

# Проверка, что код ответа 200
def test_created_order_status_code_200():
    assert order_status.status_code == 200

# Илья Дашков, 11-я когорта - Финальный проект. Инженер по тестированию плюс