from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail_goods),
    path('', views.index),
]