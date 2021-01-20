from django.shortcuts import render
from django.views.generic import DetailView
from .models import Category, Product, ProductMeta, Comment


# Create your views here.
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail_view.html'
    slug_url_kwarg = 'cat_slug'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail_view.html'
    slug_url_kwarg = 'pro_slug'
