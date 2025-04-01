import pytest
from pages.courier import CourierAPI
from helpers.helpers import generate_random_string
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"


class TestCourier:
    def setup_method(self):
        self.api = CourierAPI()

    def test_create_courier(self):

        login = generate_random_string()
        password = generate_random_string()
        first_name = generate_random_string()

        response = self.api.create_courier(login, password, first_name)
        assert response.status_code == 201
        assert response.json().get("ok") == True

    def test_duplicate_courier_creation(self):

        login = generate_random_string()
        password = generate_random_string()
        first_name = generate_random_string()

        self.api.create_courier(login, password, first_name)
        response = self.api.create_courier(login, password, first_name)
        assert response.status_code == 409
        assert "message" in response.json()

    def test_create_courier_missing_field(self):

        login = generate_random_string()
        payload = {"login": login, "password": ""}
        response = requests.post(f"{BASE_URL}/courier", json=payload)
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

    def test_courier_login(self):
        login = generate_random_string()
        password = generate_random_string()
        first_name = generate_random_string()
        self.api.create_courier(login, password, first_name)

        response = self.api.login_courier(login, password)
        assert response.status_code == 200
        assert isinstance(response.json().get("id"), int)


        courier_id = response.json().get("id")
        self.api.delete_courier(courier_id)
