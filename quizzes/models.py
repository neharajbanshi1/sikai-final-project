from django.db import models
from django.contrib.auth.models import User
from content.models import RandomTopic

# Create your models here.
class Quiz(models.Model):
    topic = models.ForeignKey(RandomTopic, on_delete=models.CASCADE, null=True)
    question = models.TextField()
    question_image = models.ImageField(upload_to='quiz_images/', blank=True)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200, blank=True)  # Optional 4th option
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    points_value = models.IntegerField(default=10)
    explanation = models.TextField(blank=True)  # Brief explanation of correct answer

    def __str__(self):
        return f"Quiz for {self.topic.title if self.topic else ''}"