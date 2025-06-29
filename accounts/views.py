from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from .models import UserProfile
from .forms import UserForm, UserProfileForm
from services.models import Service
# Login
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

# Logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('service_list')

# Registro
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

# Vista de perfil
@method_decorator(login_required, name='dispatch')
class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios'] = Service.objects.filter(autor=self.request.user)
        return context
@method_decorator(login_required, name='dispatch')
class PublicUserProfileView(DetailView):
    model = UserProfile
    template_name = 'accounts/public_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(UserProfile, user__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios'] = Service.objects.filter(autor=self.get_object().user)
        return context



# Edición del perfil (incluye datos del usuario + perfil extendido)
@method_decorator(login_required, name='dispatch')
class UserProfileUpdateView(UpdateView):
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
            'updated': False
        })

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, self.template_name, {
                'user_form': user_form,
                'profile_form': profile_form,
                'updated': True
            })

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
            'updated': False
        })
