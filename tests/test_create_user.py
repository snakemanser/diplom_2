import allure
import constants
from api_routes.user_routes import UserAPI


class TestCreateUser:

    @allure.title('Проверка создания юзера')
    @allure.description(
        'создает юзера, проверяет статус код и тело ответа, удаляет юзера')
    def test_create_user(self, del_user):
        resp = UserAPI().api_auth_register(create_data=constants.CREATE_USER_DATA)
        assert resp.status_code == 200
        assert resp.json()['success'] == True

    @allure.title('Проверка ошибки при попытке создания двух одинаковых юзеров')
    @allure.description(
        'создает юзера, создает идентичного юзера еще раз, проверяет код ошибки и тело ответа, удаляет юзера')
    def test_create_two_identical_users_error(self, prepare_user):
        resp = UserAPI().api_auth_register(create_data=constants.CREATE_USER_DATA)
        assert resp.status_code == 403
        assert resp.json()['message'] == 'User already exists'

    @allure.title('Проверка ошибки при попытке создания юзера без параметра name')
    @allure.description(
        'создает юзера без параметра name, проверяет код ошибки и тело ответа')
    def test_create_user_without_name_error(self):
        resp = UserAPI().api_auth_register(create_data=constants.CREATE_USER_DATA_NO_NAME)
        assert resp.status_code == 403
        assert resp.json()['message'] == 'Email, password and name are required fields'
