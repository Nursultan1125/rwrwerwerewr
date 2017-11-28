from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class TitleFooter(models.Model):
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    title_body = models.CharField(max_length=50, verbose_name="Тема")

    def __str__(self):
        return self.title_body

    def get_list_footer(self):
        return ListFooter.objects.filter(title_footer=self)


class ListFooter(models.Model):
    class Meta:
        verbose_name = 'Содержания'
        verbose_name_plural = 'Содержании'

    title_footer = models.ForeignKey(TitleFooter)
    list_body = models.CharField(max_length=40, verbose_name="Содержания")

    def __str__(self):
        return self.list_body


class Delivery(models.Model):
    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'
    title = models.CharField(max_length=50, verbose_name="Тема")
    body = RichTextUploadingField(verbose_name="Обзор", blank=True)

    def __str__(self):
        return self.title
