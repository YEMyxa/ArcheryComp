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
        
        return render(request, self.template_name, context={'competitions':competitions,
                                                            'discipline':self.model.DISCIPLINE_CHOICES_DICT[self.discipline],
                                                            })

class ClassicalListView(DisciplineListView):
    discipline = 'Classical'

class CompoundListView(DisciplineListView):
    discipline = 'Compound'

class DListView(DisciplineListView):
    discipline = '3D'

class AcheriListView(DisciplineListView):
    discipline = 'Acheri'

class AsymmetricalListView(DisciplineListView):
    discipline = 'Asymmetrical'


from django.views.generic import DetailView

class CompetitionDetailView(DetailView):
    model = Competition
    template_name = 'competitions/competition_detail.html'
    pk_url_kwarg = 'comp_id'

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     competition = self.object
    #     personal_participations = competition.participations.all()
    #     team_participations = competition.team_participations.all()
    #     mixed_participations = competition.mixed_participations.all()
    #     participations_type = [personal_participations, team_participations, mixed_participations]
    #     programs = set()
    #     response_html = f'<h1>{competition.title}</h1><p>{competition.description}</p>'
    #     for participations in participations_type:
    #         for participation in participations:
    #             programs.add(participation.program)
    #     for program in programs:
    #         response_html += f'<h2>{program.name}</h2><ul>'
    #         if program.team == 'Personal':
    #             participations = competition.participations.filter(program=program)
    #             for participation in participations:
    #                 update_url = reverse('competitions:update_personal',
    #                                      kwargs={'comp_id': self.kwargs['comp_id'], 'participation_id': participation.id})
    #                 response_html += (f'{participation.sportsman} {participation.place} {participation.sum_qualification} '
    #                                   f'<a href="{update_url}">Изменить</a></br>')
    #             add_url = reverse('competitions:add_personal',
    #                               kwargs={'comp_id': self.kwargs['comp_id'], 'program_id': program.id})
    #             response_html += f'<a href="{add_url}">Добавить участие</a>'
    #         elif program.team == 'Teams':
    #             response_html += f'Здесь должна быть таблица командных участий</br>'
    #             add_url = reverse('competitions:add_team',
    #                               kwargs={'comp_id': self.kwargs['comp_id'], 'program_id': program.id})
    #             response_html += f'<a href="{add_url}">Добавить участие</a>'
    #         else:
    #             response_html += f'Здесь должна быть таблица смешанных участий</br>'
    #             add_url = reverse('competitions:add_mixed',
    #                               kwargs={'comp_id': self.kwargs['comp_id'], 'program_id': program.id})
    #             response_html += f'<a href="{add_url}">Добавить участие</a>'
    #         response_html += '</ul>'
        
    #     return HttpResponse(response_html)
    
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
        print(programs)
        for program in programs:
            program.personal_program = []
            program.team_program = []
            program.mixed_program = []

            
            if program.team == 'Personal':
                participations = competition.participations.filter(program=program)
                for participation in participations:
                    program.personal_program.append([participation.sportsman,
                                                     participation.place,
                                                     participation.place_qualification,
                                                     participation.sum_qualification,
                                                     participation.id])
                program.personal_program.sort(key = lambda x: x[1])
            # Аналогично Personal     
            elif program.team == 'Teams':
                participations = competition.team_participations.filter(program=program)
                
                for participation in participations:
                    program.team_program.append([(participation.sportsman_1,
                                                  participation.sportsman_2,
                                                  participation.sportsman_3),
                                                  participation.place,
                                                  participation.place_qualification,
                                                  participation.sum_qualification,
                                                  participation.id])
                    
                program.team_program.sort(key = lambda x: x[1])
                

            else:
                participations = competition.mixed_participations.filter(program=program)
                for participation in participations:
                    program.mixed_program.append([(participation.sportsman_M,
                                                   participation.sportsman_F),
                                                   participation.place,
                                                   participation.place_qualification,
                                                   participation.sum_qualification,
                                                   participation.id])
                program.mixed_program.sort(key = lambda x: x[1])
        
        return render(request, self.template_name, context={'competition':competition,
                                                            'programs': programs,
                                                            'discipline':competition.DISCIPLINE_CHOICES_DICT[competition.discipline]})
        