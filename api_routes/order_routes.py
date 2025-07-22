import allure
import requests
import constants

class OrderAPI:

    @allure.step('Создаем заказ')
    def api_orders(self, create_data):
        path = "/api/orders"
        url = f"{constants.URL}{path}"
        return requests.post(url, data=create_data)

    @allure.step('Создаем заказ с авторизацией')
    def api_orders_auth(self, create_data, headers):
        path = "/api/orders"
        url = f"{constants.URL}{path}"
        return requests.post(url, data=create_data, headers=headers)

    @allure.step('Получаем заказ без авторизации')
    def api_orders_get(self):
        path = "/api/orders"
        url = f"{constants.URL}{path}"
        return requests.get(url)

    @allure.step('Получаем заказ с авторизацией')
    def api_orders_get_auth(self, headers):
        path = "/api/orders"
        url = f"{constants.URL}{path}"
        return requests.get(url, headers=headers)