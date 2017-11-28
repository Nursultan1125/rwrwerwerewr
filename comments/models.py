from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Comment(models.Model):
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коменты'
    comment_product = models.ForeignKey(Product)
    comment_body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    comment_author = models.ForeignKey(User)

