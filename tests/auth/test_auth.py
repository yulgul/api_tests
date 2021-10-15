from fixtures.constants import ResponseText
from fixtures.login.model import LoginUser, LoginUserResponse
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