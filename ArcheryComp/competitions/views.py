from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse
from .models import Competition

def index(request):
    classical_list_url = reverse('competitions:classical_list')
    compound_list_url = reverse('competitions:compound_list')
    D_list_url = reverse('competitions:D_list')
    acheri_list_url = reverse('competitions:acheri_list')
    asymmetrical_list_url = reverse('competitions:asymmetrical_list')
    participation_list_url = reverse('participations:main')
    html = (f"<h1>Список соревнований</h1>"
            f"<h2>Выбор дисциплины</h2>"
            f"<a href='{classical_list_url}'>Классический лук</a><br/>"
            f"<a href='{compound_list_url}'>Блочный лук</a><br/>"
            f"<a href='{D_list_url}'>3Д стрельба из лука</a><br/>"
            f"<a href='{acheri_list_url}'>Ачери</a><br/>"
            f"<a href='{asymmetrical_list_url}'>Ассиметричный лук</a><br/>"
            f"<a href='{participation_list_url}'>Список участий</a>")
    return HttpResponse(html)

from django.views.generic import ListView

def get_for_lists(self, request, *args, **kwargs):
    competitions = self.get_queryset().order_by('started_at')
    competitions_html = '<h1>Список соревнований</h1><ul>'
    for competition in competitions:
        competition_url = reverse('competitions:competition_detail', kwargs={'comp_id': competition.comp_id})
        competitions_html += f'<li><a href="{competition_url}">{competition.title}</a></li>'
    competitions_html += '</ul>'
    return HttpResponse(competitions_html)

class ClassicalListView(ListView):
    model = Competition

    def get_queryset(self):
        return Competition.objects.filter(discipline='Classical')

    get = get_for_lists

class CompoundListView(ListView):
    model = Competition

    def get_queryset(self):
        return Competition.objects.filter(discipline='Compound')

    get = get_for_lists

class DListView(ListView):
    model = Competition

    def get_queryset(self):
        return Competition.objects.filter(discipline='3D')

    get = get_for_lists

class AcheriListView(ListView):
    model = Competition

    def get_queryset(self):
        return Competition.objects.filter(discipline='Acheri')

    get = get_for_lists

class AsymmetricalListView(ListView):
    model = Competition

    def get_queryset(self):
        return Competition.objects.filter(discipline='Asymmetrical')

    get = get_for_lists

from django.views.generic import DetailView

class CompetitionDetailView(DetailView):
    model = Competition
    pk_url_kwarg = 'comp_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        competition = self.object
        personal_participations = competition.participations.all()
        team_participations = competition.team_participations.all()
        mixed_participations = competition.mixed_participations.all()
        participations_type = [personal_participations, team_participations, mixed_participations]
        programs = set()
        response_html = f'<h1>{competition.title}</h1><p>{competition.description}</p>'
        for participations in participations_type:
            for participation in participations:
                programs.add(participation.program)
        for program in programs:
            response_html += f'<h2>{program.name}</h2><ul>'
            if program.team == 'Personal':
                participations = competition.participations.filter(program=program)
                for participation in participations:
                    response_html += f'{participation.sportsman} {participation.place} {participation.sum_qualification}</br>'
            elif program.team == 'Teams':
                response_html += f'Здесь должна быть таблица командных участий'
            else:
                response_html += f'Здесь должна быть таблица смешанных участий'
            response_html += '</ul>'
        return HttpResponse(response_html)