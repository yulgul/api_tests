from requests import Response

from fixtures.login.model import LoginUser
from fixtures.validator import Validator
from common.deco import logging as log


class Auth(Validator):
    def __init__(self, app):
        self.app = app

    POST_AUTH = "/auth"

    @log("Login user")
    def login(self, data: LoginUser, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_AUTH}",
            json=data.to_dict(),
        )
        return self.structure(response, type_response=type_response)
