import datetime
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    category_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publication date', auto_now_add=True)

    def __str__(self):
        return self.category_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField('product price', default=0)
    product_description = RichTextField(blank=True, null=True)
    product_image = models.FileField(upload_to='products')
    product_pub_date = models.DateTimeField('publication date', auto_now_add=True)
    product_mod_date = models.DateTimeField('modification date', auto_now=True)
    product_disponibility = models.BooleanField(default=False)
    product_views = models.IntegerField(default=0)
    product_buy = models.IntegerField('buy link click', default=0)

    def __str__(self):
        return self.product_name

    def was_published_recently(self):
        return self.product_pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_modificated_recently(self):
        return self.product_mod_date >= timezone.now() - datetime.timedelta(days=1)

class Publicity(models.Model):
    publicity_name = models.CharField(max_length=200)
    publicity_image = models.FileField(upload_to='publicities')
    publicity_url = models.URLField('publicity website url')
    publicity_pub_date = models.DateTimeField('publication date', auto_now_add=True)
    publicity_mod_date = models.DateTimeField('modification date', auto_now=True)
    publicity_disponibility = models.BooleanField('disponibility', default=False)

    def __str__(self):
        return self.publicity_name

    def was_published_recently(self):
        return self.publicity_pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_modificated_recently(self):
        return self.publicity_mod_date >= timezone.now() - datetime.timedelta(days=1)
    