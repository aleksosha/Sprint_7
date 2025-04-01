import pytest
from pages.orders import OrdersAPI
import requests
from url import BASE_URL

class TestOrders:
    def setup_method(self):
        self.api = OrdersAPI()

    def test_create_order(self):
        response = self.api.create_order("Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2025-04-01",
                                         "Saske, come back to Konoha", ["BLACK"])
        assert response.status_code == 201
        assert "track" in response.json()

    def test_get_orders_list(self):
        response = requests.get(f"{BASE_URL}/orders")
        assert response.status_code == 200
        assert "orders" in response.json()
