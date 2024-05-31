from decimal import Decimal
from .tasks import settlement
from django.db import transaction
from django.db.models import F
from rest_framework.exceptions import NotAcceptable

from .models import User, Order


class OrderService:
    def __init__(self, user):
        self.user = user

    def create_order(self, currency: str, amount: Decimal, base_price: Decimal):
        total_cost = amount * base_price
        with transaction.atomic():
            user_balance = User.objects.filter(id=self.user.id).select_for_update().values('balance').first()['balance']

            if user_balance < total_cost:
                raise NotAcceptable({'error': 'Insufficient balance'})

            User.objects.filter(id=self.user.id).update(balance=F('balance') - total_cost)

            Order.objects.create(
                user=self.user,
                currency=currency,
                amount=amount,
                price=total_cost
            )

            settlement.apply_async(args=[currency])
