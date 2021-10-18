import pytest

from fixtures.constants import ResponseText
from fixtures.login.model import LoginUserResponse, LoginUser
from fixtures.register.model import RegisterUser, RegisterUserResponse


class TestAuthUser:
    def test_auth_user_with_valid_data(self, app):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        #"""
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data.message == ResponseText.MESSAGE_REGISTER_USER
        res = app.login.login(data=data, type_response=LoginUserResponse)
        assert res.status_code == 200

    def test_auth_created_user(self, app, auth_user_uuid_19):
        pass

    @pytest.mark.parametrize("field", ["username", "password"])
    def test_auth_invalid_data(self, app, field):
        data = LoginUser(username="kkelly@baldwin.com", password="%aP4ODss!x")
        setattr(data, field, None)
        res = app.login.login(data=data, type_response=None)
        assert res.status_code == 401
