# Generated by Django 5.2.4 on 2025-07-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='quizzes/'),
        ),
    ]
