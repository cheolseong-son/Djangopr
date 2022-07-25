from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'[{self.pk}] {self.title}'

# 상품 모델 
class Good(models.Model):  
    name = models.TextField(max_length=30)  # 상품명
    price = models.IntegerField()           # 가격

    # 상품 이미지, 이미지 무조건 올리도록 함(blank=False)
    image = models.ImageField(upload_to = 'blog/image/%Y/%m/%d/', blank=True)

    # 상품 게시 날짜와 업데이트 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

