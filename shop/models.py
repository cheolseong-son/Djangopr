from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_desctiption = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    
    # 기본값
    class Meta:
        ordering = ['name']
        verbose_name = 'category' # 단수형 이름
        verbose_name_plural = 'categories' # 복수형 이름

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])


class Product(models.Model):
    # 카테고리가 지워져도 제품은 안 지워지도록 하고, products란 이름으로 불러오게 함
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, 
    related_name= 'products') # cascade 한꺼번에 모두 지우는 것, 
    name = models.CharField(max_length=200, db_index=True)
    #  allow_unicode=True :: 한글이름 설정할 수 있도록 함
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True) 
    image = models.ImageField(upload_to= 'products/%Y/%m/%d', blank=True)
    description =  models.TextField(blank=True)# 상세페이지 설명
    meta_description = models.TextField(blank=True)
    # decimal_places : 소수점 자리, max_digits : 나타낼 자리수
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated'] # 정렬
        # 두개를 병합해서 인덱스 기준을 잡아주는 것 
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])