from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email', 'contact_num', 'contact_pub_date', 'contact_readed', 'contact_answered')
    list_filter = ('contact_answered', 'contact_readed', 'contact_pub_date')
    list_editable = ('contact_answered', 'contact_readed')
    date_hierarchy = 'contact_pub_date'

admin.site.register(Contact, ContactAdmin)
