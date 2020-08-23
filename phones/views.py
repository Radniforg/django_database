from django.shortcuts import render, redirect
from django.urls import reverse
from phones.models import Phone

def index(request):
    return redirect(reverse(show_catalog))

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    context = {'phones': phones,
               'callables': ['name', 'price', 'image',
                             'release_date', 'lte_exist']}
    return render(request, template, context)

# 'callables': ['name', 'price', 'image', 'release_date', 'lte_exist']

def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    context = {'phones': phones,
               'callables': ['name', 'price', 'image',
                             'release_date', 'lte_exist']}
    return render(request, template, context)
