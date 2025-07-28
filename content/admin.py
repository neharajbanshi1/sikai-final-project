from django.contrib import admin
from .models import TopicCategory, RandomTopic

# Register your models here.
admin.site.register(TopicCategory)
admin.site.register(RandomTopic)
