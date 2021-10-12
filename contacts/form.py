from django.forms import ModelForm

from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('contact_pub_date','contact_readed', 'contact_answered')
