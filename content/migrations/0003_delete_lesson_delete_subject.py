# Generated by Django 5.2.4 on 2025-07-28 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_topiccategory_remove_lesson_subject_randomtopic'),
        ('quizzes', '0003_remove_quiz_image_remove_quiz_lesson_and_more'),
        ('users', '0002_remove_userprofile_preferred_subjects_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
