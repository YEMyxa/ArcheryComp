from django.db import models

class Competition(models.Model):
    DISCIPLINE_CHOICES = [
        ('Classical', 'Классический лук'),
        ('Compound', 'Блочный лук'),
        ('3D', '3Д стрельба из лука'),
        ('Acheri', 'Ачери'),
        ('Asymmetrical', 'Ассиметричный лук')
    ]
    STATUS_CHOICES = [
        ('Championship', 'Чемпионат России'),
        ('Cup', 'Кубок России'),
        ('Pervenstvo', 'Первенство России'),
        ('Vseros', 'Всероссийские соревнования')
    ]

    comp_id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=250
    )
    description = models.TextField()
    discipline = models.CharField(
        max_length=50,
        choices=DISCIPLINE_CHOICES,
        default='Classical',
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
    )
    started_at = models.DateField()
    finished_at = models.DateField()
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Program(models.Model):
    DISTANCE_CHOICES = [
        (12, '12'),
        (18, '18'),
        (28, '28'),
        (30, '30'),
        (40, '40'),
        (45, '45'),
        (50, '50'),
        (60, '60'),
        (70, '70'),
        (90, '90'),
    ]
    TEAM_CHOICES = [
        ('Personal', 'Личные соревнования'),
        ('Teams', 'Командные соревнованиия'),
        ('Mixed', 'Смешанные командные соревнования')
    ]
    SEX_CHOICES = [
        ('M', 'Мужчины/Юноши'),
        ('F', 'Женщины/Девушки')
    ]

    name = models.CharField(
        max_length=100,
        unique=True,
    )
    distance_1 = models.PositiveSmallIntegerField(choices=DISTANCE_CHOICES)
    distance_2 = models.PositiveSmallIntegerField(choices=DISTANCE_CHOICES)
    shots = models.PositiveSmallIntegerField()
    finals = models.PositiveSmallIntegerField(
        choices=DISTANCE_CHOICES,
        null=True,
        blank=True,
    )
    team = models.CharField(
        max_length=10,
        choices=TEAM_CHOICES
    )
    sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES,
        null=True,
        blank=True,
    )
    age_limit = models.SmallIntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name