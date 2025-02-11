import allure
import constants
from api_routes.user_routes import UserAPI

class TestLoginUser:

    @allure.title('Логин юзера')
    @allure.description(
        'создает юзера, выполняет логин, проверяет статус код и тело ответа, удаляет юзера')
    def test_login_user(self, prepare_user):
        resp = UserAPI().api_auth_login(login_data=constants.LOGIN_USER_DATA)
        assert resp.status_code == 200
        assert resp.json()['success'] == True

    @allure.title('Логин юзера c несуществующими мейлом и паролем')
    @allure.description(
        'выполняет логин с несуществующими данными, проверяет код ошибки и тело ответа')
    def test_login_user_wrong_data_error(self):
        resp = UserAPI().api_auth_login(login_data=constants.WRONG_LOGIN_USER_DATA)
        assert resp.status_code == 401
        assert resp.json()['message'] == 'email or password are incorrect'
