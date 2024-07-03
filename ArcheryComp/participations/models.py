from django.db import models
from django.contrib.auth.models import User
from competitions.models import Competition, Program

class Sportsman(models.Model):
    SEX_CHOICES = [
        ('M', 'Мужчины/Юноши'),
        ('F', 'Женщины/Девушки')
    ]
    RANK_CHOICES = [
        ('3y', '3-й юношеский'),
        ('2y', '2-й юношеский'),
        ('1y', '1-й юношеский'),
        ('3', '3-й спортивный'),
        ('2', '2-й спортивный'),
        ('1', '1-й спортивный'),
        ('CMS', 'КМС'),
        ('MS', 'МС'),
        ('IMS', 'МСМК'),
    ]

    id = models.AutoField(primary_key=True)
    second_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES
    )
    date_of_birth = models.DateField()
    rank = models.CharField(
        max_length=10,
        choices=RANK_CHOICES,
        null=True,
        blank=True
    )
    region = models.CharField(max_length=250)
    organization = models.CharField( #в будущем может быть ForeigKey
        max_length=250,
        null=True,
        blank=True
    )
    coach = models.CharField( #в будущем может быть ForeigKey
        max_length=150,
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        User,
        related_name='data',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class PersonalParticipation(models.Model):
    competition = models.ForeignKey(
        Competition,
        related_name='participations',
        on_delete=models.CASCADE
    )
    program = models.ForeignKey(
        Program,
        related_name='participations',
        on_delete=models.RESTRICT
    )
    sportsman = models.ForeignKey(
        Sportsman,
        related_name='participations',
        on_delete=models.CASCADE
    )
    place = models.PositiveSmallIntegerField()
    place_qualification = models.PositiveSmallIntegerField()
    sum_qualification = models.PositiveSmallIntegerField()

    def __str__(self):
        return {self.place}


class TeamParticipation(models.Model):
    competition = models.ForeignKey(
        Competition,
        related_name='team_participations',
        on_delete=models.CASCADE
    )
    program = models.ForeignKey(
        Program,
        related_name='team_participations',
        on_delete=models.RESTRICT
    )
    sportsman_1 = models.ForeignKey(
        Sportsman,
        related_name='team_participations_1',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sportsman_2 = models.ForeignKey(
        Sportsman,
        related_name='team_participations_2',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sportsman_3 = models.ForeignKey(
        Sportsman,
        related_name='team_participations_3',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    place = models.PositiveSmallIntegerField()
    place_qualification = models.PositiveSmallIntegerField()
    sum_qualification = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.place

class MixedParticipation(models.Model):
    competition = models.ForeignKey(
        Competition,
        related_name='mixed_participations',
        on_delete=models.CASCADE
    )
    program = models.ForeignKey(
        Program,
        related_name='mixed_participations',
        on_delete=models.RESTRICT
    )
    sportsman_M = models.ForeignKey(
        Sportsman,
        related_name='mixed_participations_M',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sportsman_F = models.ForeignKey(
        Sportsman,
        related_name='mixed_participations_F',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    place = models.PositiveSmallIntegerField()
    place_qualification = models.PositiveSmallIntegerField()
    sum_qualification = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.place