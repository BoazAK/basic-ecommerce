import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    about_name = models.CharField(max_length=100)
    about_text = RichTextField(blank=True, null=True)
    about_pub_date = models.DateTimeField('publication date', auto_now_add=True)
    about_mod_date = models.DateTimeField('modification date', auto_now=True)

    def __str__(self):
        return self.about_name
    
    def was_published_recently(self):
        return self.about_pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_modificated_recently(self):
        return self.about_mod_date >= timezone.now() - datetime.timedelta(days=1)
        