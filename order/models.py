from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    currency = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_settled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['currency', 'is_settled']),
        ]
