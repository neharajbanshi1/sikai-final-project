from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='landing_page'), name='logout'),
]