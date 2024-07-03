from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GRADES = [
        ('1', '1 разряд'),
        ('2', '2 разряд'),
        ('3', '3 разряд'),
        ('kms', 'кандидат (КМС)'),
        ('ms', 'мастер (МС)'),
        ('msmk', 'международный (МСМК)')
        ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    club = models.CharField(max_length=100)
    grade = models.CharField(max_length=100,
                             choices=GRADES,
                             default='3')

    def __str__(self):
        return f'{self.user.username} Profile'

    