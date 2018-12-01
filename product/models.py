from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Каталог товаров'
    category_title = models.CharField(max_length=20, verbose_name="Категория")
    category_parent = models.ForeignKey('self', blank=True, null=True, default=None)
    category_slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.category_title

    def get_product(self):
        return Product.objects.filter(product_categry=self, is_public=True)


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    product_name = models.CharField(max_length=30, verbose_name="Назавания товара")
    product_overview = RichTextUploadingField(verbose_name="Обзор", blank=True)
    product_image = models.ImageField(upload_to='images/product/', verbose_name='Картинка товара')
    product_prices = models.IntegerField(verbose_name="Цена")
    product_date_create = models.DateTimeField(auto_now_add=True)
    product_date_update = models.DateTimeField(auto_now=True)
    product_categry = models.ForeignKey(Category, blank=True, null=True, default=None)
    is_public = models.BooleanField(default=False, verbose_name='Доступен')
    product_stock = models.PositiveIntegerField(verbose_name="На складе", default=0)
    product_overview_anons = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.product_name

    def get_overview_anons(self):
        return self.product_overview_anons

    def get_comments(self):
        from comments.models import Comment
        return Comment.objects.filter(comment_product=self)






