# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20170611_1533'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
