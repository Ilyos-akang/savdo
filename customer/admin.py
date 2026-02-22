from django.contrib import admin
from .models import CustomeCart,CustomeOrder,CustomeOrderItems,Customer
admin.site.register(Customer)
admin.site.register(CustomeCart)
admin.site.register(CustomeOrder)
admin.site.register(CustomeOrderItems)