from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .service import OrderService
from .models import Order
from .serializers import CreateOrderSerializer


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = Order
    permission_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            order_service = self._create_order_service(request.user)
            order_service.create_order(currency=serializer.data.get('currency'),
                                       amount=serializer.data.get('amount'),
                                       base_price=serializer.data.get('base_price')
                                       )

            return Response(status=status.HTTP_201_CREATED)

        return Response({'message': 'An error occurred while creating order.'}, status=status.HTTP_400_BAD_REQUEST)

    def _create_order_service(self, user):
        return OrderService(user=user)
