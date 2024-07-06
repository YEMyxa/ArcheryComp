from django.contrib import admin
from .models import Sportsman, PersonalParticipation, TeamParticipation, MixedParticipation

admin.site.register(Sportsman)
admin.site.register(PersonalParticipation)
admin.site.register(TeamParticipation)
admin.site.register(MixedParticipation)