from django.shortcuts import render
from django.db.models import Q
from django_app.models import Product
from django.db.models import F



def products(request):
    products = Product.objects.filter(Q(price__gt=50) | Q(quantity__lt=10))
    phone_products = Product.objects.filter(Q(name__icontains="phone") & Q(price__range=(100, 500)))
    lt_products = Product.objects.filter(~Q(price__lt=200))
    change_price_products = Product.objects.update(price=F('price') + 10)
    price_gt_products = Product.objects.filter(price__gt=F('quantity'))
    multiply_by_one_products = Product.objects.update(quantity=F('quantity') + 1)

# Create your views here.
