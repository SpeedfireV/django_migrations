from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "price", "description", )

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("product", "color", "size", "count")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("cost", "created", )

@admin.register(OrderPosition)
class OrderPositionAdmin(admin.ModelAdmin):
    list_display = ("product_type", "order", "amount", )

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "status")
