from django.contrib import admin
from .models import About

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_name', 'about_text', 'about_pub_date', 'about_mod_date')

admin.site.register(About, AboutAdmin)
