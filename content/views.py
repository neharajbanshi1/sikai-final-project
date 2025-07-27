from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Subject, Lesson

# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')

@login_required
def home(request):
    subjects = Subject.objects.all()
    return render(request, 'content/home.html', {'subjects': subjects})

@login_required
def lesson_list(request, subject_id):
    lessons = Lesson.objects.filter(subject_id=subject_id)
    return render(request, 'content/lesson_list.html', {'lessons': lessons})

@login_required
def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'content/lesson_detail.html', {'lesson': lesson})
