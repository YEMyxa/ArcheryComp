# Generated by Django 5.0.4 on 2024-06-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('comp_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('discipline', models.CharField(choices=[('Classical', 'Классический лук'), ('Compound', 'Блочный лук'), ('3D', '3Д стрельба из лука'), ('Acheri', 'Ачери'), ('Asymmetrical', 'Ассиметричный лук')], default='Classical', max_length=50)),
                ('status', models.CharField(choices=[('Championship', 'Чемпионат России'), ('Cup', 'Кубок России'), ('Pervenstvo', 'Первенство России'), ('Vseros', 'Всероссийские соревнования')], max_length=50)),
                ('started_at', models.DateField()),
                ('finished_at', models.DateField()),
                ('location', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('distance_1', models.PositiveSmallIntegerField(choices=[(12, '12'), (18, '18'), (28, '28'), (30, '30'), (40, '40'), (45, '45'), (50, '50'), (60, '60'), (70, '70'), (90, '90')])),
                ('distance_2', models.PositiveSmallIntegerField(choices=[(12, '12'), (18, '18'), (28, '28'), (30, '30'), (40, '40'), (45, '45'), (50, '50'), (60, '60'), (70, '70'), (90, '90')])),
                ('shots', models.PositiveSmallIntegerField()),
                ('finals', models.PositiveSmallIntegerField(blank=True, choices=[(12, '12'), (18, '18'), (28, '28'), (30, '30'), (40, '40'), (45, '45'), (50, '50'), (60, '60'), (70, '70'), (90, '90')], null=True)),
                ('team', models.CharField(choices=[('Personal', 'Личные соревнования'), ('Teams', 'Командные соревнованиия'), ('Mixed', 'Смешанные командные соревнования')], max_length=10)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Мужчины/Юноши'), ('F', 'Женщины/Девушки')], max_length=10, null=True)),
                ('age_limit', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]
