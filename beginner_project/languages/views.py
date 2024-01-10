from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here


class home(TemplateView):
    template_name = "home.html"


class about(TemplateView):
    template_name = "about.html"


class python(TemplateView):
    template_name = "python.html"


class fsharp(TemplateView):
    template_name = "fsharp.html"


class racket(TemplateView):
    template_name = "racket.html"
