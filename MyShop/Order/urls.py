from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from Order.views import CartView, add_to_cart
from Product.views import CategoryDetailView, ProductDetail

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    # path('cart/', add_to_cart, name='cart'),
    path('update_cart/', add_to_cart, name='update_cart'),
]