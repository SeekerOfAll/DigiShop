from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Account.forms import UserRegistrationForm


# Create your views here.
class SignInView(LoginView):
    template_name = 'login.html'


class LogoutView(LogoutView):
    template_name = 'login.html'


class SignUpView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm
