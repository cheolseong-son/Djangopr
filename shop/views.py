from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
#  get_list_or_404 : 리스트가 있으면 띄워 주고 없으면 404페이지로 보냄
from .models import *
# Create your views here.

def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    if  category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(
        request, 
        'shop/list.html',
        {
            'current_category':current_category,
            'categories':categories,
            'products':products,
        }
    )


def product_detail(request, id, product_slug=None):
    product = get_list_or_404(Product, id=id, slug = product_slug)
    return render(
        request,
        'shop/detail.html',
        {
            'product':product
        }
    )

