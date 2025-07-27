from django.urls import path
from . import views

urlpatterns = [
    path('<int:lesson_id>/', views.quiz_view, name='quiz_view'),
    path('<int:lesson_id>/results/', views.quiz_results, name='quiz_results'),
]