from django.shortcuts import render
from .models import Good, Post


def index(request):
    goods = Good.objects.all().order_by('-pk') 

    return render(
        request,
        'blog/index.html',
        {
            'goods':goods
        }
    )
# Create your views here.

def detail_goods(request, pk):
    good = Good.objects.get(pk=pk)

    return render(
        request, 
        'blog/detail.html',
        {
            'good':good,
        }
    )



