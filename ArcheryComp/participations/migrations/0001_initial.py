# Generated by Django 5.0.6 on 2024-07-08 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competitions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sportsman',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('second_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(choices=[('M', 'Мужчины/Юноши'), ('F', 'Женщины/Девушки')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('rank', models.CharField(blank=True, choices=[('3y', '3-й юношеский'), ('2y', '2-й юношеский'), ('1y', '1-й юношеский'), ('3', '3-й спортивный'), ('2', '2-й спортивный'), ('1', '1-й спортивный'), ('CMS', 'КМС'), ('MS', 'МС'), ('IMS', 'МСМК'), ('Coach', 'Организатор')], max_length=10, null=True)),
                ('region', models.CharField(max_length=250)),
                ('organization', models.CharField(blank=True, max_length=250, null=True)),
                ('coach', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.PositiveSmallIntegerField()),
                ('place_qualification', models.PositiveSmallIntegerField()),
                ('sum_qualification', models.PositiveSmallIntegerField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='competitions.competition')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='participations', to='competitions.program')),
                ('sportsman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='participations.sportsman')),
            ],
        ),
        migrations.CreateModel(
            name='MixedParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.PositiveSmallIntegerField()),
                ('place_qualification', models.PositiveSmallIntegerField()),
                ('sum_qualification', models.PositiveSmallIntegerField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mixed_participations', to='competitions.competition')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='mixed_participations', to='competitions.program')),
                ('sportsman_F', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mixed_participations_F', to='participations.sportsman')),
                ('sportsman_M', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mixed_participations_M', to='participations.sportsman')),
            ],
        ),
        migrations.CreateModel(
            name='TeamParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.PositiveSmallIntegerField()),
                ('place_qualification', models.PositiveSmallIntegerField()),
                ('sum_qualification', models.PositiveSmallIntegerField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_participations', to='competitions.competition')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='team_participations', to='competitions.program')),
                ('sportsman_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_participations_1', to='participations.sportsman')),
                ('sportsman_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_participations_2', to='participations.sportsman')),
                ('sportsman_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_participations_3', to='participations.sportsman')),
            ],
        ),
    ]
