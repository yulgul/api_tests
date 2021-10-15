from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class LoginUser(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return LoginUser(username=fake.email(), password=fake.password())


@attr.s
class LoginUserResponse:
    access_token: str = attr.ib()
