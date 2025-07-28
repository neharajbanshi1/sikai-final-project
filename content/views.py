from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TopicCategory, RandomTopic

# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')

@login_required
def home(request):
    topic_categories = TopicCategory.objects.all()
    return render(request, 'content/home.html', {'topic_categories': topic_categories})

@login_required
def lesson_list(request, category_id):
    random_topics = RandomTopic.objects.filter(category_id=category_id)
    return render(request, 'content/lesson_list.html', {'random_topics': random_topics})

@login_required
def lesson_detail(request, topic_id):
    random_topic = RandomTopic.objects.get(id=topic_id)
    return render(request, 'content/lesson_detail.html', {'random_topic': random_topic})
