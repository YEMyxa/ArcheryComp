from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse
from .models import Competition

class IndexView(View):
    template_name = 'competitions/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

from django.views.generic import ListView

class DisciplineListView(ListView):
    model = Competition
    template_name = 'competitions/discipline.html'
    discipline = ''

    def get_queryset(self):
        return Competition.objects.filter(discipline=self.discipline)

    def get(self, request, *args, **kwargs):
        competitions = self.get_queryset().order_by('started_at')
        competitions_html = '<h1>Список соревнований</h1><ul>'
        for competition in competitions:
            competition_url = reverse('competitions:competition_detail', kwargs={'comp_id': competition.comp_id})
            competitions_html += f'<li><a href="{competition_url}">{competition.title}</a></li>'
        competitions_html += '</ul>'
        return HttpResponse(competitions_html)

class ClassicalListView(DisciplineListView):
    def get_queryset(self):
        return Competition.objects.filter(discipline='Classical')

class CompoundListView(DisciplineListView):
    def get_queryset(self):
        return Competition.objects.filter(discipline='Compound')

class DListView(DisciplineListView):
    def get_queryset(self):
        return Competition.objects.filter(discipline='3D')

class AcheriListView(DisciplineListView):
    def get_queryset(self):
        return Competition.objects.filter(discipline='Acheri')

class AsymmetricalListView(DisciplineListView):
    def get_queryset(self):
        return Competition.objects.filter(discipline='Asymmetrical')

from django.views.generic import DetailView

class CompetitionDetailView(DetailView):
    model = Competition
    template_name = 'competitions/competition_detail.html'
    pk_url_kwarg = 'comp_id'


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        competition = self.object
        personal_participations = competition.participations.all()
        team_participations = competition.team_participations.all()
        mixed_participations = competition.mixed_participations.all()
        participations_type = [personal_participations, team_participations, mixed_participations]
        programs = set()

        for participations in participations_type:
            for participation in participations:
                programs.add(participation.program)

        for program in programs:
            program.personal_program = []
            program.team_program = []
            program.mixed_program = []

            participations = competition.participations.filter(program=program)
            if program.team == 'Personal':
                for participation in participations:
                    program.personal_program.append([participation.sportsman,
                                                     participation.place,
                                                     participation.place_qualification,
                                                     participation.sum_qualification,
                                                     participation.id])
            # Аналогично Personal
            elif program.team == 'Teams':
                for participation in participations:
                    program.team_program.append([(participation.sportsman_1,
                                                  participation.sportsman_2,
                                                  participation.sportsman_3),
                                                  participation.place,
                                                  participation.place_qualification,
                                                  participation.sum_qualification,
                                                  participation.id])
            else:
                for participation in participations:
                    program.mixed_program.append([(participation.sportsman_M,
                                                   participation.sportsman_F),
                                                   participation.place,
                                                   participation.place_qualification,
                                                   participation.sum_qualification,
                                                   participation.id])

        return render(request, self.template_name, context={'competition':competition,
                                                            'programs': programs,
                                                            'discipline':competition.DISCIPLINE_CHOICES_DICT[competition.discipline]})
