import pytest
import requests
from url import BASE_URL


class TestCourier:
    def test_create_courier(self, courier_api, courier_data):
        response = courier_api.create_courier(**courier_data)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    def test_duplicate_courier_creation(self, courier_api, created_courier, courier_data):
        courier_data, _ = created_courier
        response = courier_api.create_courier(**courier_data)
        assert response.status_code == 409
        assert "message" in response.json()

    @pytest.mark.parametrize(
        "payload, expected_message",
        [
            ({"login": "test_login", "password": ""}, "Недостаточно данных для создания учетной записи"),
            ({"login": "", "password": "test_password"}, "Недостаточно данных для создания учетной записи"),
        ]
    )
    def test_create_courier_missing_field(self, payload, expected_message):
        response = requests.post(f"{BASE_URL}/courier", json=payload)
        assert response.status_code == 400
        assert response.json().get("message") == expected_message

    def test_courier_login(self, courier_api, created_courier, courier_data):
        courier_data, courier_id = created_courier
        response = courier_api.login_courier(courier_data["login"], courier_data["password"])
        assert response.status_code == 200
        assert isinstance(response.json().get("id"), int)
