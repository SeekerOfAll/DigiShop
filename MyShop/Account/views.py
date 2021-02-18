from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from django.db.models import Sum
from Account.forms import UserRegistrationForm, EditProfileForm, ProfileForm

# Create your views here.
from Account.models import User
from Order.models import OrderItem


class SignInView(LoginView):
    template_name = 'login.html'


class LogoutView(LogoutView):
    template_name = 'login.html'


class SignUpView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        total_items = OrderItem.objects.aggregate(Sum("count"))
        context['total_items'] = total_items
        return context
# class UpdateProfile(UpdateView):
#     model = User
#     template_name = 'Profile_Update.html'
#     fields = ['email', 'mobile']
#
#     def get_success_url(self):
#         if 'slug' in self.kwargs:
#             slug = self.kwargs['slug']
#         else:
#             slug = 'demo'
#         return reverse('profile', kwargs={'pk': self.object.id})
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = EditProfileForm(request.POST, request.FILES, instance=request.user)
        address = ProfileForm(request.POST, instance=request.user.Address.get())

        if user.is_valid() and address.is_valid():
            user_form = user.save()
            address_form = address.save()
            address_form.user = user_form
            address_form.save()
            return redirect('profile', pk=request.user.id)
    else:
        print(request.user.Address)
        user = EditProfileForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name,
                                        'email': request.user.email, 'mobile': request.user.mobile},
                               instance=request.user.Address.get())
        address = ProfileForm(instance=request.user.Address.get())
        args = {'form': user, 'profile_form': address}
        return render(request, 'Profile_Update.html', args)
