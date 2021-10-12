from django.contrib import admin
from .models import SiteView, SiteViewsPerDay

# Register your models here.
class SiteViewAdmin(admin.ModelAdmin):
    list_display = ('view_name', 'first_view', 'last_view', 'view_count')

class SiteViewsPerDayAdmin(admin.ModelAdmin):
    list_display = ('view_day', 'first_view', 'last_view', 'views')

admin.site.register(SiteView, SiteViewAdmin)
admin.site.register(SiteViewsPerDay, SiteViewsPerDayAdmin)
