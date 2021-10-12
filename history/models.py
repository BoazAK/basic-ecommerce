import datetime
from django.db import models

# Create your models here.
class SiteView(models.Model):
    view_name = models.CharField('site views', max_length=100)
    view_count = models.IntegerField('views number', default=0)
    first_view = models.DateField('first view', auto_now_add=True)
    last_view = models.DateTimeField('last view', auto_now=True)

    def __str__(self):
        return self.view_name

class SiteViewsPerDay(models.Model):
    views = models.IntegerField('site view by day', default=0)
    view_day = models.DateField('view days', auto_now_add=True)
    first_view = models.DateTimeField('first view', auto_now_add=True)
    last_view = models.DateTimeField('last view', auto_now=True)
