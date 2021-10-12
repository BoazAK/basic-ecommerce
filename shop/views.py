import datetime
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404, redirect, reverse
from django.template import loader

from .models import Product, Category, Publicity

from history.models import  SiteView, SiteViewsPerDay
from about_page.models import About
from clicks.models import ClickOnBuyLink, ClickOnBuyLinkPerDay
from contacts.models import Contact
from contacts.form import ContactForm

# Create your views here.

def views():
    
    try:
        views = SiteView.objects.get()
        views.view_count = views.view_count + 1
        views.save()
    except ObjectDoesNotExist:
        views = SiteView(view_name='All site views', view_count=1, first_view=date.today(), last_view=timezone.now())
        views.save()

    try :
        view_day = SiteViewsPerDay.objects.filter(view_day=date.today()).get()
        view_day.views = view_day.views + 1
        view_day.save()
    except ObjectDoesNotExist:
        view_day = SiteViewsPerDay(first_view=timezone.now(), last_view=timezone.now(), views=1, view_day=date.today())
        view_day.save()
        

def index(request):
    latest_product_list = Product.objects.filter(product_disponibility=True).order_by('-product_pub_date')
    category_list = Category.objects.order_by('-id')
    publicity_list = Publicity.objects.filter(publicity_disponibility=True)
    context = {
        'latest_product_list': latest_product_list,
        'category_list': category_list,
        'publicity_list': publicity_list,
    }

    views()

    return render(request, 'shop/index.html', context)

def categorydetail(request, category_id):
    category_list = Category.objects.order_by('-id')
    publicity_list = Publicity.objects.filter(publicity_disponibility=True)
    products = get_list_or_404(Product.objects.filter(product_disponibility=True).order_by('-product_pub_date'), category=category_id)
    
    context = {
        'category_list': category_list,
        'publicity_list': publicity_list,
        'products' : products,
    }

    views()
    
    return render(request, 'shop/category.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.product_buy = product.product_buy + 1
        product.save()

        try:
            click = ClickOnBuyLink.objects.get()
            click.click = click.click +1
            click.save()
        except ObjectDoesNotExist:
            click = ClickOnBuyLink(click_name='Click on buy link', click=1, first_click=timezone.now(), last_click=timezone.now())
            click.save()

        try :
            click_day = ClickOnBuyLinkPerDay.objects.filter(click_day=date.today()).get()
            click_day.click = click_day.click + 1
            click_day.save()
        except ObjectDoesNotExist:
            click_day = ClickOnBuyLinkPerDay(click=1, first_click=timezone.now(), last_click=timezone.now(), click_day=date.today())
            click_day.save()

        urlObject = request._current_scheme_host + request.path
        
        url = 'https://wa.me/22892108027?text=J%27ai%20vu%20votre%20produit%20sur%20votre%20site%20web%20et%20je%20suis%20int%C3%A9rrress%C3%A9.%20Voici%20son%20lien%20%3A%0A' + urlObject
        return redirect(url)


    product.product_views = product.product_views + 1
    product.save()

    category_list = Category.objects.order_by('-id')
    publicity_list = Publicity.objects.filter(publicity_disponibility=True)
    context = {
        'product': product,
        'category_list': category_list,
        'publicity_list': publicity_list,
    }

    views()
    
    return render(request, 'shop/detail.html', context)

def search(request):
    response = "You're looking at the results of product."
    category_list = Category.objects.order_by('-id')
    publicity_list = Publicity.objects.filter(publicity_disponibility=True)

    views()
    
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(product_name__icontains=searched)
        products = Product.objects.filter(product_description__icontains=searched)
        products = Product.objects.filter(category__category_text__icontains=searched)

        context = {
            'searched' : searched,
            'category_list': category_list,
            'publicity_list': publicity_list,
            'products': products,
        }

        return render(request, 'shop/search.html', context)
    else:
        context = {
            'category_list': category_list,
            'publicity_list': publicity_list,
        }
        return render(request, 'shop/search.html', context)


def about(request):
    about_list = About.objects.order_by('id')
    category_list = Category.objects.order_by('-id')
    publicity_list = Publicity.objects.filter(publicity_disponibility=True)
    context = {
        'about_list': about_list,
        'category_list': category_list,
        'publicity_list': publicity_list,
    }

    views()
    
    return render(request, 'shop/about.html', context)


def service(request):
    service = 'You\'re looking at services'
    category_list = Category.objects.order_by('-id')
    publicity_list = Publicity.objects.filter(publicity_disponibility=True)

    context = {
        'service': service,
        'category_list': category_list,
        'publicity_list': publicity_list,
    }

    views()
    
    return render(request, 'shop/service.html', context)

    
def contact(request):
    category_list = Category.objects.order_by('-id')
    publicity_list = Publicity.objects.filter(publicity_disponibility=True)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ContactForm()

    context = {
        "form": form,
        'category_list': category_list,
        'publicity_list': publicity_list,
    }

    views()
    
    return render(request, 'shop/contact.html', context)
