from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatbotSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat session for {self.user.username} at {self.created_at}"
