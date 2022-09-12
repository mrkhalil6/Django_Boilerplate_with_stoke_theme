from django.contrib import admin
from .models import Product, Warehouse, ChargesPerWarehouse


# Register your models here.
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(ChargesPerWarehouse)
