from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from homeView.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="homeView"),
]
