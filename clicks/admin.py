from django.contrib import admin
from .models import ClickOnBuyLink, ClickOnBuyLinkPerDay

# Register your models here.
class ClickOnBuyLinkAdmin(admin.ModelAdmin):
    list_display = ('click_name', 'first_click', 'last_click', 'click')

class ClickOnBuyLinkPerDayAdmin(admin.ModelAdmin):
    list_display = ('click_day', 'first_click', 'last_click', 'click')
    date_hierarchy = 'last_click'

admin.site.register(ClickOnBuyLink, ClickOnBuyLinkAdmin)
admin.site.register(ClickOnBuyLinkPerDay, ClickOnBuyLinkPerDayAdmin)
