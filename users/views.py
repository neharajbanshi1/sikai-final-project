from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, UserProfileForm, LoginForm

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page after registration
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserProfileForm()
    return render(request, 'users/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def landing_page(request):
    return render(request, 'landing.html')

def profile(request):
    return render(request, 'users/profile.html')
