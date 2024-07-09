# Generated by Django 5.0.6 on 2024-07-09 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participations', '0002_alter_sportsman_first_name_alter_sportsman_id_and_more'),
        ('users', '0002_profile_sport_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportsman',
            name='user',
        ),
        migrations.AddField(
            model_name='sportsman',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to='users.profile'),
        ),
    ]
