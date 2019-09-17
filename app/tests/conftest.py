import pytest
from funcy import first, second

from config import create_app


@pytest.fixture(scope="session")
def setup_env():
    return create_app.create_app(debug=True, testing=True)


@pytest.fixture(scope="session")
def app(setup_env):
    return first(setup_env)


@pytest.fixture(scope="session")
def es(setup_env):
    return second(setup_env)


@pytest.fixture
def hotel_reviews():
    import json

    with open("workflows/dry_provider/booking_hotel_reviews.json") as f:
        return json.load(f)
