# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models
from aerolab.settings import MEDIA_ROOT


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


def folder_exists(path):
    return (os.path.isdir(MEDIA_ROOT + path))


def category_folder(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<category_name>/<filename>
    path = '{0}/'.format(instance.category.name)
    if not folder_exists(path):
        os.mkdir(MEDIA_ROOT + path)
    return path + '{0}'.format(filename)


class Item(models.Model):
    category = models.ForeignKey(Category)
    description = models.CharField(max_length=30)
    image = models.ImageField(upload_to=category_folder)  # MEDIA_ROOT

    def __str__(self):
        return '{} - {}'.format(self.description, self.category)
