from django.contrib import admin
from .models import Order, User


class OrderAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)
