from django.db import models
from django.contrib.auth.models import User
from competitions.models import Competition, Program
from users.models import Profile
from django.contrib.auth.models import User

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
        User,
        related_name='participations',
        on_delete=models.CASCADE
    )
    place = models.PositiveSmallIntegerField()
    place_qualification = models.PositiveSmallIntegerField()
    sum_qualification = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.sportsman}, {self.competition}'


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
        User,
        related_name='team_participations_1',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sportsman_2 = models.ForeignKey(
        User,
        related_name='team_participations_2',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sportsman_3 = models.ForeignKey(
        User,
        related_name='team_participations_3',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    place = models.PositiveSmallIntegerField()
    place_qualification = models.PositiveSmallIntegerField()
    sum_qualification = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'({self.sportsman_1}, {self.sportsman_2}, {self.sportsman_3}) {self.competition}'

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
        User,
        related_name='mixed_participations_M',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sportsman_F = models.ForeignKey(
        User,
        related_name='mixed_participations_F',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    place = models.PositiveSmallIntegerField()
    place_qualification = models.PositiveSmallIntegerField()
    sum_qualification = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'({self.sportsman_M}, {self.sportsman_F}) {self.competition}'