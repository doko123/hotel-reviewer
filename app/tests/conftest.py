from config import create_app
import pytest
from funcy import first, second


@pytest.fixture(scope="session")
def setup_env():
    return create_app.create_app(debug=True, testing=True)


@pytest.fixture(scope="session")
def app(setup_env):
    return first(setup_env)


@pytest.fixture(scope="session")
def es(setup_env):
    return second(setup_env)
