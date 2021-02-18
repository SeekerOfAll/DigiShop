from django.urls import path
from Account.views import SignInView, LogoutView, SignUpView, ProfileView, edit_profile

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/<slug:pk>/', ProfileView.as_view(), name='profile'),
    path('update/', edit_profile, name='update_profile'),
]
