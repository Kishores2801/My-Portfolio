# Generated by Django 4.0.1 on 2022-06-11 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_blog_thumbnail_alter_project_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Deepnote_url',
        ),
        migrations.RemoveField(
            model_name='project',
            name='github_url',
        ),
    ]