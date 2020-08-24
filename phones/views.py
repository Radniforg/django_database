from django.shortcuts import render, redirect
from django.urls import reverse
from phones.models import Phone

def index(request):
    return redirect(reverse(show_catalog))

def show_catalog(request):
    template = 'catalog.html'
    page_type = request.GET.get('sort')
    if page_type == 'name':
        phones = Phone.objects.all().order_by('name')
    elif page_type == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif page_type == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones,
               'callables': ['name', 'image', 'price']}
    return render(request, template, context)

# 'callables': ['name', 'price', 'image', 'release_date', 'lte_exist']

def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    context = {'phones': phones,
               'callables': ['name', 'image', 'price',
                             'release_date', 'lte_exist']}
    return render(request, template, context)
