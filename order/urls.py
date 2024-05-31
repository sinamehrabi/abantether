from django.urls import path
from .apis import OrderViewSet
from rest_framework import routers

api_router = routers.SimpleRouter()
api_router.register("", OrderViewSet, basename='order_viewset')
urlpatterns = [
    path('', OrderViewSet.as_view({'post': 'create'}), name='order')
]
