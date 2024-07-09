from django.contrib import admin
from .models import PersonalParticipation, TeamParticipation, MixedParticipation


# @admin.register(Sportsman)
# class SportsmanAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'last_name', 'first_name', 'second_name', 'sex', 'date_of_birth', 'rank', 'region', 'organization',
#         'coach')
#     list_filter = ('sex', 'rank')
#     search_fields = ('id', 'second_name', 'date_of_birth', 'region', 'organization')
#     list_editable = ('rank', 'region', 'organization', 'coach')


@admin.register(PersonalParticipation)
class PersonalParticipationAdmin(admin.ModelAdmin):
    list_display = ('competition', 'program', 'sportsman', 'place', 'place_qualification', 'sum_qualification')


@admin.register(TeamParticipation)
class TeamParticipationAdmin(admin.ModelAdmin):
    list_display = (
        'competition', 'program', 'sportsman_1', 'sportsman_2', 'sportsman_3', 'place', 'place_qualification',
        'sum_qualification')


@admin.register(MixedParticipation)
class MixedParticipationAdmin(admin.ModelAdmin):
    list_display = (
        'competition', 'program', 'sportsman_M', 'sportsman_F', 'place', 'place_qualification', 'sum_qualification')