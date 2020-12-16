from django.contrib import admin
# Register your models here.

from .models import Product,ProductGallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','exist', 'price', 'active']
    list_editable = ['active']
    list_filter = ['exist','active']
    search_fields = ['title','description']
    list_per_page = 20
    class Meta:
        model = Product



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
