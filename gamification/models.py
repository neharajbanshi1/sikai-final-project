from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Badge(models.Model):
    BADGE_TYPES = [
        ('topic_explorer', 'Topic Explorer'),
        ('quiz_master', 'Quiz Master'),
        ('game_champion', 'Game Champion'),
        ('daily_learner', 'Daily Learner'),
        ('perfect_score', 'Perfect Score'),
        ('category_expert', 'Category Expert'),
    ]
    
    BADGE_LEVELS = [
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    badge_type = models.CharField(max_length=20, choices=BADGE_TYPES)
    badge_level = models.CharField(max_length=10, choices=BADGE_LEVELS)
    icon = models.CharField(max_length=50)  # Font Awesome icon
    criteria = models.JSONField()  # Criteria for earning the badge
    points_required = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    progress_data = models.JSONField(blank=True, null=True)  # Progress toward next level
    
    class Meta:
        unique_together = ['user', 'badge']

    def __str__(self):
        return f"{self.user.username} - {self.badge.name}"

class ActivityLog(models.Model):
    ACTIVITY_TYPES = [
        ('quiz_completed', 'Quiz Completed'),
        ('game_played', 'Mini Game Played'),
        ('topic_explored', 'Topic Explored'),
        ('badge_earned', 'Badge Earned'),
        ('level_up', 'Level Up'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    points_earned = models.IntegerField(default=0)
    details = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} at {self.created_at}"
