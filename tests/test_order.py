import allure
import pytest
import constants
from api_routes.user_routes import UserAPI
from api_routes.order_routes import OrderAPI


class TestCreateOrder:

    @allure.title('Проверка создания заказа')
    @allure.description(
        'создает заказ, проверяет статус код и тело ответа')
    def test_create_order(self):
        resp = OrderAPI().api_orders(create_data=constants.CREATE_ORDER_DATA)
        assert resp.status_code == 200
        assert resp.json()['success'] == True

    @allure.title('Проверка создания заказа с некорректными данными')
    @allure.description(
        'создает заказ с неверным хешем, потом с пустым списком, проверяет  код ошибки и тело ответа')
    @pytest.mark.parametrize('data', [
        constants.CREATE_ORDER_DATA_WRONG_HASH,
        constants.CREATE_ORDER_DATA_EMPTY
    ])
    def test_create_order_wrong_data_error(self, data):
        resp = OrderAPI().api_orders(create_data=data)
        if data == constants.CREATE_ORDER_DATA_WRONG_HASH:
            assert resp.status_code == 500
        else:
            assert resp.status_code == 400
            assert resp.json()['message'] == 'Ingredient ids must be provided'

    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description(
        'создает юзера, создает заказ, проверяет статус код и тело ответа, удаляет юзера')
    def test_create_order_auth(self, prepare_user):
        access_token = UserAPI().api_auth_login(login_data=constants.LOGIN_USER_DATA).json()['accessToken']
        headers = {'Authorization': f'{access_token}'}
        resp = OrderAPI().api_orders_auth(create_data=constants.CREATE_ORDER_DATA, headers=headers)
        assert resp.status_code == 200
        assert resp.json()['order']['owner']['name'] == 'Pudge'


class TestGetOrder:

    @allure.title('Проверка получаения заказа с авторизацией')
    @allure.description(
        'создает юзера, создает заказ, получает заказ для юзера, проверяет статус код и название бургера')
    def test_get_order_auth(self, prepare_user):
        access_token = UserAPI().api_auth_login(login_data=constants.LOGIN_USER_DATA).json()['accessToken']
        headers = {'Authorization': f'{access_token}'}
        OrderAPI().api_orders_auth(create_data=constants.CREATE_ORDER_DATA, headers=headers)
        resp = OrderAPI().api_orders_get_auth(headers=headers)
        assert resp.status_code == 200
        assert resp.json()['orders'][0]['name'] == 'Бессмертный флюоресцентный бургер'

    @allure.title('Проверка получаения заказа без авторизации')
    @allure.description(
        'получает заказ, проверяет код ошибки и тело ответа')
    def test_get_order_anauth(self):
        resp = OrderAPI().api_orders_get()
        assert resp.status_code == 401
        assert resp.json()['message'] == 'You should be authorised'