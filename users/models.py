from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(10)])
    preferred_subjects = models.ManyToManyField('content.Subject', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cluster_group = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
