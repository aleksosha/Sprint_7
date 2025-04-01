import requests

class OrdersAPI:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

    def create_order(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }
        return requests.post(self.BASE_URL, json=payload)
