from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import PersonalParticipation, TeamParticipation, MixedParticipation
from django.contrib.auth.models import User
from users.models import Profile
from django.db.models import Q
from django.views.generic import ListView
from .forms import PersonalParticipationForm, TeamParticipationForm, MixedParticipationForm
from competitions.models import Competition, Program

class SportsmanListView(ListView):
    model = User
    template_name = 'participations/sportsman_list.html'
 

    def get(self,  request, *args, **kwargs):
        sportsmans = self.get_queryset().order_by('last_name')
        return render(request, self.template_name, context={'sportsmans': sportsmans}) 

class PersonalParticipationListView(ListView):
    model = PersonalParticipation
    template_name = 'participations/user_participation.html'
    def get(self, request, *args, **kwargs):
        
        participations = PersonalParticipation.objects.filter(sportsman__username=self.kwargs['username'])
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
        participations = TeamParticipation.objects.filter(Q(sportsman_1__username=self.kwargs['username'])
                                                          | Q(sportsman_2__username=self.kwargs['username'])
                                                          | Q(sportsman_3__username=self.kwargs['username']))
        participations_html = '<h2>Список командных участий</h2><ul>'
        for participation in participations:
            competition = participation.competition
            competition_url = reverse('competitions:competition_detail',
                                      kwargs={'comp_id': competition.comp_id})
            team = [participation.sportsman_1, participation.sportsman_2, participation.sportsman_3]
            team.remove(get_object_or_404(User, username=self.kwargs['username']))
            if competition != competition_prev:
                participations_html += f'<a href="{competition_url}">{participation.competition.title}</a></br>'
            participations_html += (f'<li>    {participation.program.name} {participation.place} '
                                    f'{participation.place_qualification} {participation.sum_qualification}</br>'
                                    f'в команде с ')
            for i in range(2):
                teammate_url = reverse('users:profile_view', kwargs={'username': team[i].username})
                participations_html += f'<a href="{teammate_url}">{team[i].last_name} {team[i].first_name} </a>'
            participations_html += '</li>'
            competition_prev = competition
        participations_html += '</ul>'
        return HttpResponse(participations_html)

# class TeamParticipationListView(ListView):
#     model = TeamParticipation
#     template_name = 'participations/user_teamparticipation.html'

    
    

    # def get(self, request, *args, **kwargs):
    #     competition_prev = 0
    #     participations = TeamParticipation.objects.filter(Q(sportsman_1__username=self.kwargs['username'])
    #                                                       | Q(sportsman_2__username=self.kwargs['username'])
    #                                                       | Q(sportsman_3__username=self.kwargs['username']))
    #     competitions = {}

    #     for participation in participations:
    #         if not competitions.get(participation.competition):
    #             competitions.update({participation.competition:[]})
            
    #         team = [participation.sportsman_2, participation.sportsman_3]
    #         team.remove(get_object_or_404(User, username=self.kwargs['username']))
    #         competitions.get(participation.competition).append([participation,
    #                                                            team])
            
    #         competition = participation.competition
    #         competition_url = reverse('competitions:competition_detail',
    #                                   kwargs={'comp_id': competition.comp_id})
            
            
    #         if competition != competition_prev:
    #             participations_html += f'<a href="{competition_url}">{participation.competition.title}</a></br>'
    #         participations_html += (f'<li>    {participation.program.name} {participation.place} '
    #                                 f'{participation.place_qualification} {participation.sum_qualification}</br>'
    #                                 f'в команде с ')
    #         for i in range(2):
    #             teammate_url = reverse('users:profile_view', kwargs={'username': team[i].username})
    #             participations_html += f'<a href="{teammate_url}">{team[i].last_name} {team[i].first_name} </a>'
    #         participations_html += '</li>'
    #         competition_prev = competition
    #     participations_html += '</ul>'
        
    #     competitions = [[key]+value for key, value in competitions.items()]
        
    #     return render(request, self.template_name, context={'competitions': competitions})


class MixedParticipationListView(ListView):
    model = MixedParticipation

    def get(self, request, *args, **kwargs):
        competition_prev = 0
        sportsman = User.objects.get(username=self.kwargs['username'])
        if sportsman.profile.sex == 'M':
            participations = MixedParticipation.objects.filter(sportsman_M__username = self.kwargs['username'])
        else:
            participations = MixedParticipation.objects.filter(sportsman_F__username = self.kwargs['username'])
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
            if sportsman.profile.sex == 'M':
                teammate = participation.sportsman_F
            else:
                teammate = participation.sportsman_M
            teammate_url = reverse('users:profile_view', kwargs={'username': teammate.username})
            participations_html += f'<a href="{teammate_url}">{teammate.last_name} {teammate.first_name} </a>'
            participations_html += '</li>'
            competition_prev = competition
        participations_html += '</ul>'
        return HttpResponse(participations_html)

def profile(request, username):
    template_name = 'participations/user_partisipations.html'
    return render(request, template_name, context={'username': username})

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