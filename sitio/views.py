# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def home(request):
    titulo = "Instituto Tecnológico Nacional De México"
    subtitulo = "Instituto Tecnolóngico De Tijuana"
    context = {
        "titulo": titulo,
        "subTitulo": subtitulo
    }
    return render(request, "sitio/home.html", context)
