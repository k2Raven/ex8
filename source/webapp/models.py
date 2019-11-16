from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0], verbose_name='Категория')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Товар')
    text_review = models.TextField(max_length=3000, verbose_name='Текст отзыва')
    rating =models.IntegerField(verbose_name='Оценка')