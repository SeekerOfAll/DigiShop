from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from Product.views import CategoryDetailView, ProductDetailView

urlpatterns = [

    path('search/<slug:cat_slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<slug:pro_slug>/', ProductDetailView.as_view(), name='product_detail'),
]
