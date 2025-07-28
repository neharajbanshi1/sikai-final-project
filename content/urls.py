from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('category/<int:category_id>/', views.lesson_list, name='lesson_list'),
    path('topic/<int:topic_id>/', views.lesson_detail, name='lesson_detail'),
]