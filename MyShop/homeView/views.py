from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from Product.models import Category, Product, Brand
from homeView.models import SlideShow


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = SlideShow.objects.all()
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        context['brands'] = Brand.objects.all()
        return context
