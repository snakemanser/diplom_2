import allure
import pytest
import constants
from api_routes.user_routes import UserAPI


class TestChangeDataUser:

    @allure.title('Проверка изменения данных юзера')
    @allure.description(
        'создает юзера, изменяет мейл, потом имя, проверяет статус код и тело ответа, удаляет юзера')
    @pytest.mark.parametrize('new_data,new_login_data', [
        (constants.PATCH_USER_DATA_EMAIL, constants.PATCH_DELETE_DATA_EMAIL),
        (constants.PATCH_USER_DATA_NAME, constants.PATCH_DELETE_DATA_NAME)
    ])
    def test_patch_user_data(self, new_data, new_login_data):
        UserAPI().api_auth_register(create_data=constants.CREATE_USER_DATA)
        resp = UserAPI().api_auth_user_patch(login_data=constants.LOGIN_USER_DATA, new_data=new_data)
        if new_data == constants.PATCH_USER_DATA_EMAIL:
            assert resp.status_code == 200
            assert resp.json()['user']['email'] == 'test_bu4ka322@yandex.ru'
            UserAPI().api_auth_user_delete(login_data=new_login_data)
        else:
            assert resp.status_code == 200
            assert resp.json()['user']['name'] == 'Pudge322'
            UserAPI().api_auth_user_delete(login_data=new_login_data)

    @allure.title('Проверка изменения данных юзера без авторизации')
    @allure.description(
        'создает юзера, изменяет мейл, потом имя, проверяет код ошибки и тело ответа, удаляет юзера')
    @pytest.mark.parametrize('new_data', [
        constants.PATCH_USER_DATA_EMAIL,
        constants.PATCH_USER_DATA_NAME
    ])
    def test_patch_user_data_anauth_error(self, prepare_user, new_data):
        resp = UserAPI().api_user_patch_anauth(new_data=new_data)
        assert resp.status_code == 401
        assert resp.json()['message'] == 'You should be authorised'
