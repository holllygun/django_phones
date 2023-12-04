import csv
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting = request.GET.get("sort")
    if sorting == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sorting == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sorting == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    phone_objects = Phone.objects.filter(slug=slug).values_list('name', 'price', 'lte_exist', 'image', 'release_date')
    phones_dict = {
        'name': phone_objects[0][0],
        'price': phone_objects[0][1],
        'lte_exists': phone_objects[0][2],
        'image': phone_objects[0][3],
        'release_date': phone_objects[0][4],

    }

    template = 'product.html'
    context = {'phone': phones_dict}
    return render(request, template, context)
