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

