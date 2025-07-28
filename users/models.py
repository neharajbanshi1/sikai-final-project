from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(10)])
    favorite_topics = models.ManyToManyField('content.TopicCategory', blank=True)
    current_level = models.IntegerField(default=1)
    total_points = models.IntegerField(default=0)
    daily_streak = models.IntegerField(default=0)
    last_activity_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cluster_group = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
