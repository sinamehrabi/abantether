from django.db import transaction
from .models import Order
from abantether import celery_app


def buy_from_exchange(currency, total_amount):
    print(f"Simulating settlement for {total_amount} of {currency}")


@celery_app.task()
def settlement(currency):
    with (transaction.atomic()):
        orders = Order.objects.select_for_update(skip_locked=True).filter(currency=currency, is_settled=False)
        total_amount = 0
        total_price = 0
        for item in orders:
            total_amount += item.amount
            total_price += item.price

        if total_price >= 10.0:
            buy_from_exchange(currency, total_amount)
            for order in orders:
                order.is_settled = True
                order.save()
