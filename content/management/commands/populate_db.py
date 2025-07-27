from django.core.management.base import BaseCommand
from content.models import Subject, Lesson

class Command(BaseCommand):
    help = 'Populates the database with sample subjects and lessons'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing subjects and lessons...')
        Subject.objects.all().delete()
        Lesson.objects.all().delete()

        self.stdout.write('Creating sample subjects...')
        math = Subject.objects.create(name='Math', description='Learn about numbers and shapes.', age_groups='3-5,6-8')
        science = Subject.objects.create(name='Science', description='Explore the world around you.', age_groups='6-8,9-10')
        art = Subject.objects.create(name='Art', description='Unleash your creativity.', age_groups='3-5,6-8,9-10')

        self.stdout.write('Creating sample lessons...')
        Lesson.objects.create(
            title='Counting to 10',
            content='Learn to count from 1 to 10 with fun animations.',
            subject=math,
            age_group='3-5',
            difficulty_level=1
        )
        Lesson.objects.create(
            title='Basic Shapes',
            content='Learn to identify circles, squares, and triangles.',
            subject=math,
            age_group='3-5',
            difficulty_level=1
        )
        Lesson.objects.create(
            title='Introduction to Addition',
            content='Learn how to add small numbers together.',
            subject=math,
            age_group='6-8',
            difficulty_level=2
        )
        Lesson.objects.create(
            title='The Solar System',
            content='Explore the planets in our solar system.',
            subject=science,
            age_group='6-8',
            difficulty_level=2
        )
        Lesson.objects.create(
            title='What are Plants?',
            content='Learn about the different parts of a plant.',
            subject=science,
            age_group='6-8',
            difficulty_level=1
        )
        Lesson.objects.create(
            title='The Water Cycle',
            content='Learn how water moves around the Earth.',
            subject=science,
            age_group='9-10',
            difficulty_level=3
        )
        Lesson.objects.create(
            title='Drawing with Colors',
            content='Learn to mix and use different colors in your drawings.',
            subject=art,
            age_group='3-5',
            difficulty_level=1
        )
        Lesson.objects.create(
            title='Creating a Collage',
            content='Learn how to make a collage from different materials.',
            subject=art,
            age_group='6-8',
            difficulty_level=2
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data.'))