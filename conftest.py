import pytest

from fixtures.app import StoreApp


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
