from django.contrib import admin
from django.urls import path, include
from django.template.loader import render_to_string
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('admin/',          admin.site.urls),
    path('',                views.IndexView.as_view(), name='home_page'),
    path('competitions/',   include('competitions.urls',   namespace='competitions')),
    path('participations/', include('participations.urls', namespace='participations')),
    path('users/',          include(('users.urls', 'users'), namespace='users')),
]
