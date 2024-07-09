from django.contrib import admin
from .models import Competition, Program


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        'comp_id', 'title', 'discipline', 'status', 'started_at', 'finished_at', 'location')
    list_filter = ('discipline', 'status')
    search_fields = ('comp_id', 'title', 'description', 'location')
    list_editable = ('status', 'location', 'discipline')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'distance_1', 'distance_2', 'shots', 'finals', 'team', 'sex', 'age_limit')
    list_filter = ('distance_1', 'distance_2', 'team', 'sex')
    search_fields = ('name',)
    list_editable = ('distance_1', 'distance_2', 'team', 'sex')