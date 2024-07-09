from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import PersonalParticipation, TeamParticipation, MixedParticipation
from django import forms

class PersonalParticipationForm(ModelForm):
    class Meta:
        model = PersonalParticipation
        fields = ['sportsman',
                  'place', 'place_qualification', 'sum_qualification']
        
        labels = {'sportsman':'Спортсмен', 
                  'place':'Место',
                  'place_qualification':'Место в квалификации',
                  'sum_qualification':'Сумма в квалификации'}
        
class TeamParticipationForm(ModelForm):
    class Meta:
        model = TeamParticipation
        fields = ['sportsman_1', 'sportsman_2', 'sportsman_3',
                  'place', 'place_qualification', 'sum_qualification']
        
        labels = {'sportsman_1':'Спортсмен 1',
                  'sportsman_2':'Спортсмен 2',
                  'sportsman_3':'Спортсмен 3', 
                  'place':'Место',
                  'place_qualification':'Место в квалификации',
                  'sum_qualification':'Сумма в квалификации'}

class MixedParticipationForm(ModelForm):
    class Meta:
        model = MixedParticipation
        fields = ['sportsman_M', 'sportsman_F',
                  'place', 'place_qualification', 'sum_qualification']
        
        labels = {'sportsman_M':'Спортсмен М',
                  'sportsman_F':'Спортсмен Ж', 
                  'place':'Место',
                  'place_qualification':'Место в квалификации',
                  'sum_qualification':'Сумма в квалификации'}


class PersonalProgramForm(ModelForm):
    class Meta:
        model = PersonalParticipation
        fields = ['program',
                  'sportsman',
                  'place', 'place_qualification', 'sum_qualification']

        labels = {'sportsman': 'Спортсмен',
                  'place': 'Место',
                  'place_qualification': 'Место в квалификации',
                  'sum_qualification': 'Сумма в квалификации'}

class TeamProgramForm(ModelForm):
    class Meta:
        model = TeamParticipation
        fields = ['program',
                  'sportsman_1', 'sportsman_2', 'sportsman_3',
                  'place', 'place_qualification', 'sum_qualification']

        labels = {'sportsman': 'Спортсмен',
                  'place': 'Место',
                  'place_qualification': 'Место в квалификации',
                  'sum_qualification': 'Сумма в квалификации'}

class MixedProgramForm(ModelForm):
    class Meta:
        model = MixedParticipation
        fields = ['program',
                  'sportsman_M', 'sportsman_F',
                  'place', 'place_qualification', 'sum_qualification']

        labels = {'sportsman': 'Спортсмен',
                  'place': 'Место',
                  'place_qualification': 'Место в квалификации',
                  'sum_qualification': 'Сумма в квалификации'}