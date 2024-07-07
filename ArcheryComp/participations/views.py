from django.http import HttpResponse
from django.urls import reverse
from .models import PersonalParticipation, TeamParticipation, MixedParticipation

def index(request):
    html = f"<h1>Список участий</h1>"
    return HttpResponse(html)

from django.views.generic import CreateView
from .forms import PersonalParticipationForm, TeamParticipationForm, MixedParticipationForm
from django.shortcuts import render, redirect, get_object_or_404
from competitions.models import Competition, Program

class ParticipationCreateView(CreateView):
    template_name = 'participations/add_participation.html'

    def form_valid(self, form):
        form.instance.competition = get_object_or_404(Competition, pk=self.kwargs['comp_id'])
        form.instance.program = get_object_or_404(Program, pk=self.kwargs['program_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('competitions:competition_detail', kwargs={'comp_id': self.kwargs['comp_id']})

class PersonalParticipationCreateView(ParticipationCreateView):
    model = PersonalParticipation
    form_class = PersonalParticipationForm

class TeamParticipationCreateView(ParticipationCreateView):
    model = TeamParticipation
    form_class = TeamParticipationForm

class MixedParticipationCreateView(ParticipationCreateView):
    model = MixedParticipation
    form_class = MixedParticipationForm

from django.views.generic.edit import UpdateView

class ParticipationUpdateView(UpdateView):
    template_name = 'participations/update_participation.html'
    pk_url_kwarg = 'participation_id'

    def get_success_url(self):
        return reverse('competitions:competition_detail', kwargs={'comp_id': self.kwargs['comp_id']})

class PersonalParticipationUpdateView(ParticipationUpdateView):
    model = PersonalParticipation
    form_class = PersonalParticipationForm

class TeamParticipationUpdateView(ParticipationUpdateView):
    model = TeamParticipation
    form_class = TeamParticipationForm

class MixedParticipationUpdateView(ParticipationUpdateView):
    model = MixedParticipation
    form_class = MixedParticipationForm