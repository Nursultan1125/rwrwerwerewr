# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer_data', '0003_auto_20170623_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Тема'),
        ),
    ]
