from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_info = Phone.objects.all()
    sort_filter = request.GET.get('sort')
    if sort_filter == 'name':
        phones_info = phones_info.order_by('name')
    elif sort_filter == 'min_price':
        phones_info = phones_info.order_by('price')
    elif sort_filter == 'max_price':
        phones_info = phones_info.order_by('-price')
    context = {
        'phones': phones_info
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_info = Phone.objects.filter(slug__exact=slug)
    context = {
        'phone': phone_info[0]
    }
    return render(request, template, context)
