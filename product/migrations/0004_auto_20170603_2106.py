# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20170603_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=30, verbose_name='Нзавания товара'),
        ),
    ]
