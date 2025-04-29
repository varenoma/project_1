from django.shortcuts import render, get_object_or_404
from .models import Product


def show_products(request):
    products = Product.objects.filter(in_stock = True)
    return render(request, 'product/home.html', {'data': products})


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product/product_detail.html', {'product': product})
