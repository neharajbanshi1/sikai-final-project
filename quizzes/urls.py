from django.urls import path
from . import views

urlpatterns = [
    path('topic/<int:topic_id>/', views.quiz_view, name='take_quiz'),
    path('results/<int:topic_id>/', views.quiz_results, name='quiz_results'),
]