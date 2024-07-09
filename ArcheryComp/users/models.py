from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    SEX_CHOICES = [
        ('M', 'Мужчины/Юноши'),
        ('F', 'Женщины/Девушки')
    ]

    RANK_CHOICES = [
        ('3-й юношеский', '3-й юношеский'),
        ('2-й юношеский', '2-й юношеский'),
        ('1-й юношеский', '1-й юношеский'),
        ('3-й спортивный', '3-й спортивный'),
        ('2-й спортивный', '2-й спортивный'),
        ('1-й спортивный', '1-й спортивный'),
        ('КМС', 'КМС'),
        ('МС', 'МС'),
        ('МСМК', 'МСМК'),
        ('Организатор', 'Организатор'),
        ('Нет разряда', 'Нет разряда'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # sport_id = models.IntegerField(unique=True, null=True)

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
    
    date_of_birth = models.DateField(null=True, blank=True)

    rank = models.CharField(
        max_length=20,
        choices=RANK_CHOICES,
        default='-',
        null=True,
        blank=True
    )
    region = models.CharField(max_length=250, null=True, blank=True)

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

    