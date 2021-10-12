from django.contrib import admin
from .models import Category, Product, Publicity

# Register your models here.
class PublicityAdmin(admin.ModelAdmin):
    list_display = ('publicity_name', 'publicity_url', 'publicity_pub_date', 'publicity_mod_date', 'publicity_disponibility')
    list_filter = ('publicity_disponibility', 'publicity_pub_date', 'publicity_mod_date')
    list_editable = ['publicity_disponibility']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_pub_date', 'product_mod_date', 'product_buy', 'product_views', 'product_disponibility')
    list_filter = ('category', 'product_disponibility', 'product_pub_date', 'product_mod_date')
    list_editable = ('product_disponibility', 'product_price')
    list_per_page = 10
    date_hierarchy = 'product_pub_date'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_text', 'pub_date')
    list_filter = ['pub_date']

admin.site.site_header = 'E-Commerce'
admin.site.site_title = 'E-Commerce'

admin.site.register(Publicity, PublicityAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
