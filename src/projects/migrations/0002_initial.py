# Generated by Django 4.0.5 on 2022-06-08 17:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='users', through='users.Contributor', to=settings.AUTH_USER_MODEL),
        ),
    ]
