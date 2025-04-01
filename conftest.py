import pytest
from pages.courier import CourierAPI

@pytest.fixture
def courier_api():
    return CourierAPI()