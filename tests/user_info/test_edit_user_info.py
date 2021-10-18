import pytest

from fixtures.constants import ResponseText
from fixtures.user_info.model import (
    AddUserInfo,
    AddUserInfoResponse,
    PutUserInfoResponse,
)


class TestPutUserInfo:
    def test_edit_user_info_with_valid_data(self, app, auth_user):
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
        data = AddUserInfo.random()
        res = app.userinfo.edit_user_info(
            user_id=auth_user.uuid,
            data=data,
            header=auth_user.header,
            type_response=PutUserInfoResponse,
        )
        assert res.status_code == 200
        assert res.data.message == ResponseText.MESSAGE_UPDATE_USER_INFO

    @pytest.mark.parametrize("field", ["phone", "email"])
    def test_edit_user_with_empty_one_field(self, app, auth_user_uuid_19, field):
        data = AddUserInfo.random()
        setattr(data, field, None)
        res = app.userinfo.edit_user_info(
            user_id=auth_user_uuid_19.uuid,
            data=data,
            header=auth_user_uuid_19.header,
            type_response=PutUserInfoResponse,
        )
        assert res.status_code == 200
        assert res.data.message == ResponseText.MESSAGE_UPDATE_USER_INFO
