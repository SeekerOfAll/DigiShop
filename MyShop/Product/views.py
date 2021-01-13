from django.shortcuts import render
from django.views.generic import DetailView
from .models import Category


# Create your views here.
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail_view.html'
    slug_url_kwarg = 'cat_slug'
