from django.shortcuts import render
from django.views.generic import ListView, DetailView

from webapp.models import Product


class IndexView(ListView):
    model = Product
    template_name = 'index.html'

class ProductView( DetailView):
    model = Product
    template_name = 'product/detail.html'