from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)  # Math, Science, Language, Art
    description = models.TextField()
    age_groups = models.CharField(max_length=20)  # "3-5", "6-8", "9-10"

    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    age_group = models.CharField(max_length=10)
    difficulty_level = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])
    image = models.ImageField(upload_to='lessons/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
