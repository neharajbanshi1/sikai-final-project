# Generated by Django 5.2.4 on 2025-07-28 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=50)),
                ('color_theme', models.CharField(max_length=7)),
                ('age_groups', models.CharField(max_length=20)),
                ('unlock_level', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
        migrations.CreateModel(
            name='RandomTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('fun_fact', models.TextField()),
                ('age_group', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='topics/')),
                ('difficulty_level', models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.topiccategory')),
            ],
        ),
    ]
