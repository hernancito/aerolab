# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Item


def catalogo(request):
    items = Item.objects.all().order_by("date")
    total_items = items.count()
    items = items[:16]
    context = {
        'title': "Catálogo",
        'item_list': items,
        'total_items': total_items
    }

    return render(request, 'catalogo/index.html', context)
