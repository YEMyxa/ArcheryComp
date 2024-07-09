from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
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
        ('Coach', 'Организатор'),
        ('-', 'б/р'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    second_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES,
        default='M',
    )
    
    date_of_birth = models.DateField(null=True,)

    rank = models.CharField(
        max_length=10,
        choices=RANK_CHOICES,
        default='-',
        null=True,
        blank=True
    )
    region = models.CharField(max_length=250, null=True,)

    organization = models.CharField( #в будущем может быть ForeigKey
        max_length=250,
        null=True,
        blank=True,
    )
    
    coach = models.CharField( #в будущем может быть ForeigKey
        max_length=150,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    