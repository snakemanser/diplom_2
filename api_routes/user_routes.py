import allure
import requests
import constants


class UserAPI:

    @allure.step('Создаем юзера')
    def api_auth_register(self, create_data):
        path = "/api/auth/register"
        url = f"{constants.URL}{path}"
        return requests.post(url, data=create_data)

    @allure.step('Логин юзера')
    def api_auth_login(self, login_data):
        path = "/api/auth/login"
        url = f"{constants.URL}{path}"
        return requests.post(url, data=login_data)

    @allure.step('Удаляем юзера')
    def api_auth_user_delete(self, login_data):
        access_token = self.api_auth_login(login_data).json()['accessToken']
        headers = {'Authorization': f'{access_token}'}
        path = f"/api/auth/user"
        url = f"{constants.URL}{path}"
        return requests.delete(url, headers=headers)

    @allure.step('Изменяем данные юзера')
    def api_auth_user_patch(self, login_data, new_data):
        access_token = self.api_auth_login(login_data).json()['accessToken']
        headers = {'Authorization': f'{access_token}'}
        path = f"/api/auth/user"
        url = f"{constants.URL}{path}"
        return requests.patch(url, data=new_data, headers=headers)

    @allure.step('Изменяем данные юзера без авторизации')
    def api_user_patch_anauth(self, new_data):
        path = f"/api/auth/user"
        url = f"{constants.URL}{path}"
        return requests.patch(url, data=new_data)
