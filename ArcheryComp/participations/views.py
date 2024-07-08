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
    html = f"<h1>Список участий</h1>"
    return HttpResponse(html)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'participations/index.html')
    

class UserParticipitionsView(View):
    def get(self,  request, username, *args, **kwargs):
        return render(request, 'participations/user_part.html', context={'username': username})