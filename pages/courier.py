import requests

class CourierAPI:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

    def create_courier(self, login, password, first_name):
        payload = {"login": login, "password": password, "firstName": first_name}
        return requests.post(self.BASE_URL, json=payload)

    def login_courier(self, login, password):
        payload = {"login": login, "password": password}
        return requests.post(f"{self.BASE_URL}/login", json=payload)

    def delete_courier(self, courier_id):
        return requests.delete(f"{self.BASE_URL}/{courier_id}")