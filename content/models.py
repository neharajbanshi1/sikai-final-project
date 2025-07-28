from django.db import models

# Create your models here.
class TopicCategory(models.Model):
    name = models.CharField(max_length=50)  # Animals, Space, Numbers, etc.
    description = models.TextField()
    icon = models.CharField(max_length=50)  # Font Awesome icon class
    color_theme = models.CharField(max_length=7)  # Hex color code
    age_groups = models.CharField(max_length=20)
    unlock_level = models.IntegerField(default=1)  # Level required to unlock

    def __str__(self):
        return self.name

class RandomTopic(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(TopicCategory, on_delete=models.CASCADE)
    content = models.TextField()  # Brief, engaging content
    fun_fact = models.TextField()  # Interesting fact about the topic
    age_group = models.CharField(max_length=10)
    image = models.ImageField(upload_to='topics/', blank=True)
    difficulty_level = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
