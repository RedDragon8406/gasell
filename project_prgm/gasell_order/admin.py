from django.contrib import admin

# Register your models here.
from gasell_order.models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_paid', 'payment_date']
    list_filter = ['is_paid', 'payment_date']
    search_fields = ['owner', 'payment_date']
    list_per_page = 10


class OrderAdminDetail(admin.ModelAdmin):
    list_display = ['order', '__str__', 'price', 'count']
    list_filter = ['product']
    search_fields = ['__str__']
    list_per_page = 10


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderAdminDetail)
