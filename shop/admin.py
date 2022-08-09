from django.contrib import admin
from .models import *


# Register your models here.
# 등록방법 1
class CategroryAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    # prepopulated_fields = {'slug':['name',]} # 위 아래 다 튜플, 리스트 가능

admin.site.register(Category, CategroryAmin)

# 등록방법 2 : 언어테이션 기법
@admin.register(Product)
class ProductAmin(admin.ModelAdmin):
    list_display = ['id', 'name','slug', 'category', 'price','stock',
    'available_display', 'available_order', 'created', 'updated']
    list_filter = ['available_display','created', 'updated', 'category']
    prepopulated_fields = {'slug':['name',]}
    list_editable = ['price', 'stock', 'available_display', 'available_order']