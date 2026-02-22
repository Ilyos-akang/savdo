from django.contrib import admin
from .models import Category,ProductInput,Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInput)