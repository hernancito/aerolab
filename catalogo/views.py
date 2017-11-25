# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def catalogo(request):
    context = {
        'title': "Catálogo"
    }

    return render(request, 'catalogo/index.html', context)
