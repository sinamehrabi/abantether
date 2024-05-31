from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Order
from decimal import Decimal


class CurrencyBasePrices:
    ABAN = Decimal(4.00)


class CreateOrderSerializer(serializers.ModelSerializer):
    base_price = serializers.SerializerMethodField(allow_null=False)

    class Meta:
        model = Order
        fields = ['currency', 'amount', 'base_price']

    def get_base_price(self, obj):
        if hasattr(CurrencyBasePrices, obj.get('currency')):
            return getattr(CurrencyBasePrices, obj.get('currency'))
        raise ValidationError(detail={"Message": f"{obj.get('currency')} currency not supported!"})
