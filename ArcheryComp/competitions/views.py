from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse
# from .models import Project, Task
from django.template.loader import render_to_string
# from .forms import ProjectForm, TaskForm
from django.contrib.auth.mixins import PermissionRequiredMixin

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

def classical_list(request):
    return HttpResponse("<h1>Cписок соревнований: Классический лук</h1>")

def compound_list(request):
    return HttpResponse("<h1>Cписок соревнований: Блочный лук</h1>")

def D_list(request):
    return HttpResponse("<h1>Cписок соревнований: 3Д стрельба из лука</h1>")

def acheri_list(request):
    return HttpResponse("<h1>Cписок соревнований: Ачери</h1>")

def asymmetrical_list(request):
    return HttpResponse("<h1>Cписок соревнований: Ассиметричный лук</h1>")

def competition_detail(request, competition_id):
    return HttpResponse(f"Информация о соревновании {competition_id}")


class IndexView(View):
    template_name = 'competitions/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)