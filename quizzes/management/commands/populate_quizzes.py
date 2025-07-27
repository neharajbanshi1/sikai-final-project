from django.core.management.base import BaseCommand
from content.models import Lesson
from quizzes.models import Quiz

class Command(BaseCommand):
    help = 'Populates the database with sample quizzes for existing lessons'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing quizzes...')
        Quiz.objects.all().delete()

        self.stdout.write('Creating sample quizzes...')
        
        lessons = Lesson.objects.all()
        
        for lesson in lessons:
            if lesson.title == 'Counting to 10':
                Quiz.objects.create(
                    lesson=lesson,
                    question='What comes after 5?',
                    option_a='6',
                    option_b='7',
                    option_c='8',
                    correct_answer='A'
                )
                Quiz.objects.create(
                    lesson=lesson,
                    question='What is 2 + 3?',
                    option_a='4',
                    option_b='5',
                    option_c='6',
                    correct_answer='B'
                )
            elif lesson.title == 'Basic Shapes':
                Quiz.objects.create(
                    lesson=lesson,
                    question='Which shape has 3 sides?',
                    option_a='Circle',
                    option_b='Square',
                    option_c='Triangle',
                    correct_answer='C'
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample quizzes.'))