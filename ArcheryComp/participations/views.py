from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import Sportsman, PersonalParticipation, TeamParticipation, MixedParticipation
from django.db.models import Q

from django.views.generic import ListView

class SportsmanListView(ListView):
    model = Sportsman
    template_name = 'participations/sportsman_list.html'

    def get(self,  request, *args, **kwargs):
        sportsmans = self.get_queryset().order_by('last_name')
        sportsmans_html = '<h1>Список спортсменов</h1><ul>'
        for sportsman in sportsmans:
            profile_url = reverse('users:profile_view', kwargs={'username': sportsman.profile.user.username})
            sportsmans_html += f'<li><a href="{profile_url}">{sportsman.last_name} {sportsman.first_name}</a></li>'
        sportsmans_html += '</ul>'
        return HttpResponse(sportsmans_html)

class PersonalParticipationListView(ListView):
    model = PersonalParticipation
    template_name = 'participations/user_participation.html'
    
    def get(self,  request, *args, **kwargs):
        participations = self.model.objects.filter(sportsman=self.kwargs['id'])
        competitions = {}
        for participation in participations:
            if not competitions.get(participation.competition):
                competitions.update({participation.competition:[]})
            competitions.get(participation.competition).append(participation)
        
        return render(request, self.template_name, context={'competitions': competitions})

class TeamParticipationListView(ListView):
    model = TeamParticipation

    def get(self, request, *args, **kwargs):
        competition_prev = 0
        participations = TeamParticipation.objects.filter(Q(sportsman_1=self.kwargs['id'])
                                                          | Q(sportsman_2=self.kwargs['id'])
                                                          | Q(sportsman_3=self.kwargs['id']))
        participations_html = '<h2>Список командных участий</h2><ul>'
        for participation in participations:
            competition = participation.competition
            competition_url = reverse('competitions:competition_detail',
                                      kwargs={'comp_id': competition.comp_id})
            team = [participation.sportsman_1, participation.sportsman_2, participation.sportsman_3]
            team.remove(get_object_or_404(Sportsman, pk=self.kwargs['id']))
            if competition != competition_prev:
                participations_html += f'<a href="{competition_url}">{participation.competition.title}</a></br>'
            participations_html += (f'<li>    {participation.program.name} {participation.place} '
                                    f'{participation.place_qualification} {participation.sum_qualification}</br>'
                                    f'в команде с ')
            for i in range(2):
                teammate_url = reverse('users:profile_view', kwargs={'username': team[i].profile.user.username})
                participations_html += f'<a href="{teammate_url}">{team[i].last_name} {team[i].first_name} </a>'
            participations_html += '</li>'
            competition_prev = competition
        participations_html += '</ul>'
        return HttpResponse(participations_html)

class MixedParticipationListView(ListView):
    model = MixedParticipation

    def get(self, request, *args, **kwargs):
        competition_prev = 0
        participations = PersonalParticipation.objects.filter(sportsman=self.kwargs['id'])
        participations_html = '<h2>Список личных участий</h2><ul>'
        for participation in participations:
            competition = participation.competition
            competition_url = reverse('competitions:competition_detail',
                                      kwargs={'comp_id': competition.comp_id})
            if competition != competition_prev:
                participations_html += f'<a href="{competition_url}">{participation.competition.title}</a></br>'
            participations_html += (f'<li>    {participation.program.name} {participation.place} '
                                    f'{participation.place_qualification} {participation.sum_qualification}</li>')
            competition_prev = competition
        participations_html += '</ul>'
        return HttpResponse(participations_html)

class TeamParticipationListView(ListView):
    model = TeamParticipation

    def get(self, request, *args, **kwargs):
        competition_prev = 0
        participations = TeamParticipation.objects.filter(Q(sportsman_1=self.kwargs['id'])
                                                          | Q(sportsman_2=self.kwargs['id'])
                                                          | Q(sportsman_3=self.kwargs['id']))
        participations_html = '<h2>Список командных участий</h2><ul>'
        for participation in participations:
            competition = participation.competition
            competition_url = reverse('competitions:competition_detail',
                                      kwargs={'comp_id': competition.comp_id})
            team = [participation.sportsman_1, participation.sportsman_2, participation.sportsman_3]
            team.remove(get_object_or_404(Sportsman, pk=self.kwargs['id']))
            if competition != competition_prev:
                participations_html += f'<a href="{competition_url}">{participation.competition.title}</a></br>'
            participations_html += (f'<li>    {participation.program.name} {participation.place} '
                                    f'{participation.place_qualification} {participation.sum_qualification}</br>'
                                    f'в команде с ')
            for i in range(2):
                teammate_url = reverse('users:profile_view', kwargs={'username': team[i].profile.user.username})
                participations_html += f'<a href="{teammate_url}">{team[i].last_name} {team[i].first_name} </a>'
            participations_html += '</li>'
            competition_prev = competition
        participations_html += '</ul>'
        return HttpResponse(participations_html)

class MixedParticipationListView(ListView):
    model = MixedParticipation

    def get(self, request, *args, **kwargs):
        competition_prev = 0
        sportsman = get_object_or_404(Sportsman, pk=self.kwargs['id'])
        if sportsman.sex == 'M':
            participations = MixedParticipation.objects.filter(sportsman_M = self.kwargs['id'])
        else:
            participations = MixedParticipation.objects.filter(sportsman_F=self.kwargs['id'])
        participations_html = '<h2>Список смешанных командных участий</h2><ul>'
        for participation in participations:
            competition = participation.competition
            competition_url = reverse('competitions:competition_detail',
                                      kwargs={'comp_id': competition.comp_id})
            if competition != competition_prev:
                participations_html += f'<a href="{competition_url}">{participation.competition.title}</a></br>'
            participations_html += (f'<li>    {participation.program.name} {participation.place} '
                                    f'{participation.place_qualification} {participation.sum_qualification}</br>'
                                    f'в команде с ')
            if sportsman.sex == 'M':
                teammate = participation.sportsman_F
            else:
                teammate = participation.sportsman_M
            teammate_url = reverse('users:profile_view', kwargs={'username': teammate.profile.user.username})
            participations_html += f'<a href="{teammate_url}">{teammate.last_name} {teammate.first_name} </a>'
            participations_html += '</li>'
            competition_prev = competition
        participations_html += '</ul>'
        return HttpResponse(participations_html)

def profile(request, id):
    participations_list_url = reverse('participations:participations_list', kwargs={'id': id})
    team_participations_list_url = reverse('participations:team_participations_list', kwargs={'id': id})
    mixed_participations_list_url = reverse('participations:mixed_participations_list', kwargs={'id': id})
    html = (f'<h1>Участия спортсмена {id}</h1>'
            f'<a href="{participations_list_url}">Список личных участий</a></br>'
            f'<a href="{team_participations_list_url}">Список командных участий</a></br>'
            f'<a href="{mixed_participations_list_url}">Список смешанных командных участий</a>')
    return HttpResponse(html)

from django.views.generic import CreateView
from .forms import PersonalParticipationForm, TeamParticipationForm, MixedParticipationForm
from django.shortcuts import render, redirect, get_object_or_404
from competitions.models import Competition, Program

class ParticipationCreateView(CreateView):
    template_name = 'participations/add_participation.html'

    def form_valid(self, form):
        form.instance.competition = get_object_or_404(Competition, pk=self.kwargs['comp_id'])
        form.instance.program =     get_object_or_404(Program,     pk=self.kwargs['program_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('competitions:competition_detail', kwargs={'comp_id': self.kwargs['comp_id']})
    

class PersonalParticipationCreateView(PermissionRequiredMixin, ParticipationCreateView):
    model = PersonalParticipation
    form_class = PersonalParticipationForm
    permission_required = 'participations.add_personalparticipation'


class TeamParticipationCreateView(PermissionRequiredMixin, ParticipationCreateView):
    model = TeamParticipation
    form_class = TeamParticipationForm
    permission_required = 'participations.add_teamparticipation'

class MixedParticipationCreateView(PermissionRequiredMixin, ParticipationCreateView):
    model = MixedParticipation
    form_class = MixedParticipationForm
    permission_required = 'participations.add_mixedparticipation'

class ParticipationUpdateView(UpdateView):
    template_name = 'participations/update_participation.html'
    pk_url_kwarg = 'participation_id'

    def get_success_url(self):
        return reverse('competitions:competition_detail', kwargs={'comp_id': self.kwargs['comp_id']})
    
class PersonalParticipationUpdateView(PermissionRequiredMixin, ParticipationUpdateView):
    model = PersonalParticipation
    form_class = PersonalParticipationForm
    permission_required = 'participations.change_personalparticipation'

class TeamParticipationUpdateView(PermissionRequiredMixin, ParticipationUpdateView):
    model = TeamParticipation
    form_class = TeamParticipationForm
    permission_required = 'participations.change_teamparticipation'

class MixedParticipationUpdateView(PermissionRequiredMixin, ParticipationUpdateView):
    model = MixedParticipation
    form_class = MixedParticipationForm
    permission_required = 'participations.change_mixedparticipation'


class UserParticipitionsView(View):
    def get(self,  request, username, *args, **kwargs):
        return render(request, 'participations/user_part.html', context={'username': username})

class ParticipationDeleteView(DeleteView):
    model = None
    pk_url_kwarg = 'participation_id'
    success_url = reverse_lazy('competitions:competition_detail')
    template_name = 'participation/delete_participation.html'

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'participation':self.get_object()})

class PersonalParticipationDeleteView(PersonalParticipationUpdateView):
    model = PersonalParticipation