# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=10000),
            preserve_default=False,
        ),
    ]