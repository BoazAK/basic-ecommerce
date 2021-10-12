import datetime
from django.db import models

# Create your models here.
class ClickOnBuyLink(models.Model):
    click_name = models.CharField('click', max_length=100)
    click = models.IntegerField('click number', default=0)
    first_click = models.DateField('first click', auto_now_add=True)
    last_click = models.DateTimeField('last click', auto_now=True)

    def __str__(self):
        return self.click_name

class ClickOnBuyLinkPerDay(models.Model):
    click = models.IntegerField('all click on buy link', default=0)
    click_day = models.DateField('click days', auto_now_add=True)
    first_click = models.DateTimeField('first click', auto_now_add=True)
    last_click = models.DateTimeField('last click', auto_now=True)
