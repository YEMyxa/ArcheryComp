from django.forms import ModelForm
from .models import PersonalParticipation, TeamParticipation, MixedParticipation

class PersonalParticipationForm(ModelForm):
    class Meta:
        model = PersonalParticipation
        fields = ['sportsman',
                  'place', 'place_qualification', 'sum_qualification']

class TeamParticipationForm(ModelForm):
    class Meta:
        model = TeamParticipation
        fields = ['sportsman_1', 'sportsman_2', 'sportsman_3',
                  'place', 'place_qualification', 'sum_qualification']

class MixedParticipationForm(ModelForm):
    class Meta:
        model = MixedParticipation
        fields = ['sportsman_M', 'sportsman_F',
                  'place', 'place_qualification', 'sum_qualification']
