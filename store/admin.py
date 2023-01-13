from django.contrib import admin
from .models import *

admin.site.register(Photo)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ShippingAddress)
admin.site.register(Contact)


"""
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'customer')
    list_filter = ('transaction_id', 'customer')
    search_fields = ('name', 'email')
"""


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'customer', 'product', 'quantity', 'price', 'date_added')
