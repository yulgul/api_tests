from fixtures.constants import ResponseText

from fixtures.user_info.model import (
    AddUserInfo,
    AddUserInfoResponse,
    DeleteUserInfoResponse,
    GetUserInfoResponse,
)


class TestGetUserInfo:
    def test_get_user_info_with_valid_data(self, app, auth_user):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        #"""
        data = AddUserInfo.random()
        res = app.userinfo.add_info(
            user_id=auth_user.uuid,
            data=data,
            header=auth_user.header,
            type_response=AddUserInfoResponse,
        )
        assert res.status_code == 200
        assert res.data.message == ResponseText.MESSAGE_ADD_USER_INFO
        res = app.userinfo.delete_user_info(
            user_id=auth_user.uuid,
            header=auth_user.header,
            type_response=DeleteUserInfoResponse,
        )
        assert res.status_code == 200
        assert res.data.message == ResponseText.MESSAGE_DELETE_USER_INFO
        res = app.userinfo.get_user_info(
            user_id=auth_user.uuid,
            header=auth_user.header,
            type_response=GetUserInfoResponse,
        )
        assert res.status_code == 404
