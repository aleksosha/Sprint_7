import pytest
from pages.courier import CourierAPI
from helpers.helpers import generate_random_string

@pytest.fixture(scope="function")
def courier_api():
    return CourierAPI()

@pytest.fixture
def courier_data():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "first_name": generate_random_string(),
    }

@pytest.fixture
def created_courier(courier_api, courier_data):
    response = courier_api.create_courier(**courier_data)
    assert response.status_code == 201
    assert response.json().get("ok") is True

    login_response = courier_api.login_courier(courier_data["login"], courier_data["password"])
    assert login_response.status_code == 200
    courier_id = login_response.json().get("id")

    yield courier_data, courier_id

    courier_api.delete_courier(courier_id)
