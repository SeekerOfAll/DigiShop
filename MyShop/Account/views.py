from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from django.db.models import Sum
from Account.forms import UserRegistrationForm, EditProfileForm, ProfileForm, SignInForm

# Create your views here.
from Account.models import User
from Order.models import OrderItem


class SignInView(LoginView):
    template_name = 'login.html'
    form_class = SignInForm
    redirect_authenticated_user = True
    success_url = 'homeView'

    # def get_queryset(self):
    #     queryset = super(SignInView, self).get_queryset()
    #     print(self.request.POST)
    #     return queryset
    # success_message = 'Welcome to your profile'


class LogoutView(LogoutView):
    template_name = 'login.html'


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return super(SignUpView, self).form_valid(form)


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        total_items = OrderItem.objects.aggregate(Sum("count"))
        context['total_items'] = total_items
        return context


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
        # obj, created = Person.objects.get_or_create(
        #     first_name='John',
        #     last_name='Lennon',
        #     defaults={'birthday': date(1940, 10, 9)},
        # )
        print(request.user.Address)
        try:
            address = request.user.Address.get()
        except:
            address, created = request.user.Address.get_or_create(city='city',street='street',alley='alley',zip_code='0')
            address.save()
        user = EditProfileForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name,
                                        'email': request.user.email, 'mobile': request.user.mobile},
                               instance=request.user.Address.get())
        # instance = request.user.Address.get()
        # if request.user.Address:
        #     address = ProfileForm(instance=request.user.Address.get())
        # else:
        #     address = ProfileForm(request.user.Address.)
        address = ProfileForm(instance=request.user.Address.get())
        args = {'form': user, 'profile_form': address}
        return render(request, 'profile_update.html', args)
