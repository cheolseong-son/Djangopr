from django.urls import path
from . import views

urlpatterns = [
    # path('create/', views.create_page),
    path('create/', views.CreatePage.as_view()),
    path('<int:pk>/', views.detail_goods),
    path('', views.index),
]