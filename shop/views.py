from math import ceil

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # allProds = [[products, range(1, len(products)), nSlides], [products, range(1, len(products)), nSlides]]
    # param = {'allProds': allProds}

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        param = {'allProds': allProds}

    return render(request, "shop/index2.html", param)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("contact")


def search(request):
    return HttpResponse("search")


def prodView(request):
    return HttpResponse("product")


def checkout(request):
    return HttpResponse("checkout")
