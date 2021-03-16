from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from Account.models import Address

User = get_user_model()


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}))



# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True, 'autofocus': True}))
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}))
#     remember_me = forms.BooleanField(required=False)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_('Password'), required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Repeat Password'), required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'mobile', 'password', 'password2',)
        labels = {'email': _('Email'), 'password': _('Password'), 'mobile': _('Mobile'),
                  'password2': _('Repeat Password'), 'first_name': _('First Name'), 'last_name': _('Last Name'), }

        widget = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control'}),
                  # 'password': forms.PasswordInput(),
                  # # 'mobile': forms.CharField(attrs={'class': 'form-control'}),
                  # 'password2': forms.PasswordInput(),
                  'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                  'last_name': forms.TextInput(attrs={'class': 'form-control'}), }

        # help_text = {'email': _('A valid email for reset your password'), }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'mobile', 'image')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('city', 'street', 'alley', 'zip_code')
