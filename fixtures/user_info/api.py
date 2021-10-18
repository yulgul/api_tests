from requests import Response

from fixtures.user_info.model import AddUserInfo
from fixtures.validator import Validator
from common.deco import logging as log


class UserInfo(Validator):
    def __init__(self, app):
        self.app = app

    POST_USER_INFO = "/user_info/{}"

    @log("Add user info")
    def add_info(
        self, user_id: int, data: AddUserInfo, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Get user info")
    def get_user_info(self, user_id: int, header=None, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser # noqa
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_id)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Delete user info")
    def delete_user_info(
        self, user_id: int, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser # noqa
        """
        response = self.app.client.request(
            method="DELETE",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_id)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Edit user info")
    def edit_user_info(
        self, user_id: int, data: AddUserInfo, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser # noqa
        """
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)
