import datetime
from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_num = models.CharField('contact number', max_length=25)
    contact_body = models.TextField()
    contact_pub_date = models.DateTimeField('publication date', auto_now_add=True)
    contact_readed = models.BooleanField('read statut', default=False)
    contact_answered = models.BooleanField('answer statut', default=False)

    def __str__(self):
        return self.contact_name
