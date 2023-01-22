from django.contrib import admin
from .models import *


admin.site.register(Photo)
admin.site.register(Order)
admin.site.register(ShippingAddress)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'manufacturer',
        'price',
        )
    prepopulated_fields = {'slug': ('title',)}


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'customer',
        'product',
        'quantity',
        'price',
        'date_added',
        )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
