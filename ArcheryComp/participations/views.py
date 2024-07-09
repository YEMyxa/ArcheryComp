from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from .models import PersonalParticipation, TeamParticipation, MixedParticipation
from django.views.generic import CreateView
from .forms import PersonalParticipationForm, TeamParticipationForm, MixedParticipationForm
from competitions.models import Competition, Program

def index(request):
    html = f"<h1>Список спортсменов</h1>"
    return HttpResponse(html)



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

