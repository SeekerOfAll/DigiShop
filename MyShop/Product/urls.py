from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from Product import views
from Product.views import CategoryDetailView, ProductDetail, SearchResultsView, create_comment

urlpatterns = [
    path('category/<slug:cat_slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<slug:pro_slug>/', ProductDetail.as_view(), name='product_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('comment/', create_comment, name='comment_create'),
]
