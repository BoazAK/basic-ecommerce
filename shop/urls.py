from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('produit/<int:product_id>/', views.detail, name='detail'),
    path('category/<int:category_id>/', views.categorydetail, name='categorydetail'),
    path('search/', views.search, name='search'),
    path('about.html/', views.about, name='about'),
    path('service.html/', views.service, name='service'),
    path('contact.html/', views.contact, name='contact'),
]
