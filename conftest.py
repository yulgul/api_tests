import pytest

from fixtures.app import StoreApp
from fixtures.login.model import LoginUserResponse, AuthUserType, LoginUser
from fixtures.register.model import RegisterUser, RegisterUserResponse


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    return StoreApp(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        default="https://stores-tests-api.herokuapp.com",
        help="enter api url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="kkelly@baldwin.com",
        help="enter userlogin",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="%aP4ODss!x",
        help="enter password",
    ),


@pytest.fixture()
def auth_user(app):
    data = RegisterUser.random()
    res_register = app.register.register(data=data, type_response=RegisterUserResponse)
    res_auth = app.login.login(data=data, type_response=LoginUserResponse)
    user_id = res_register.data.uuid
    token = res_auth.data.access_token
    header = {"Authorization": f"JWT {token}"}
    return AuthUserType(user_id, header)


@pytest.fixture()
def auth_user_uuid_19(app, request):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    auth_data = LoginUser(username=username, password=password)
    res_auth = app.login.login(data=auth_data, type_response=LoginUserResponse)
    user_id = 19
    token = res_auth.data.access_token
    header = {"Authorization": f"JWT {token}"}
    return AuthUserType(user_id, header)
