from django.shortcuts import render, redirect
from .models import Good
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class CreatePage(LoginRequiredMixin, CreateView):
    model = Good
    fields = ['name', 'price', 'image']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(CreatePage, self).form_valid(form)
        else:
            return redirect('/shopping/')
            
        # return redirect('/shopping/')





# def create_page(request):
#     return render(
#         request,
#         'blog/create_page.html',
#     )