from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('subject/<int:subject_id>/', views.lesson_list, name='lesson_list'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
]