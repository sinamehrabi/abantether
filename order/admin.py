from django.contrib import admin
from .models import Order, User


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'is_settled')


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)
