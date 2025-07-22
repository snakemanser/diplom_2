import pytest
import constants
from api_routes.user_routes import UserAPI

@pytest.fixture(scope='function')
def prepare_user():
    user = UserAPI().api_auth_register(create_data=constants.CREATE_USER_DATA)
    yield user
    UserAPI().api_auth_user_delete(login_data=constants.LOGIN_USER_DATA)

@pytest.fixture(scope='function')
def del_user():
    yield
    UserAPI().api_auth_user_delete(login_data=constants.LOGIN_USER_DATA)

