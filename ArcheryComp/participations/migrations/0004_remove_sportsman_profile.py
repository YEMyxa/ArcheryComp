# Generated by Django 5.0.6 on 2024-07-09 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participations', '0003_remove_sportsman_user_sportsman_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportsman',
            name='profile',
        ),
    ]
