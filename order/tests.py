from base64 import b64encode
from decimal import Decimal

from .models import Order, User
from rest_framework.test import APITestCase


class OrderModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='sina', password='sina1234', balance=100)
        cls.headers = {
            "Authorization": "Basic {}".format(
                b64encode(bytes(f"sina:sina1234", "utf-8")).decode("ascii")
            )
        }

    def test_order_create(self):
        response = self.client.post("/orders/", {'currency': "ABAN", 'amount': 3}, format="json",
                                    headers=self.headers)
        order = Order.objects.first()

        assert response.status_code == 201
        assert order.currency == "ABAN"
        assert order.amount == Decimal(3)

    def test_order_create_with_insufficient_balance(self):
        response = self.client.post("/orders/", {'currency': "ABAN", 'amount': 30}, format="json",
                                    headers=self.headers)

        orders = Order.objects.all()
        assert response.status_code == 406
        assert len(orders) == 0
