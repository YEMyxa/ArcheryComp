from django.urls import path, include
from . import views
from . import forms

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/',  views.ProfileUpdateView.as_view(), name='profile'),
    path('profile/<str:username>/',  views.ProfileDetailView.as_view(), name='profile_view'),
    path('login/',    views.MyLoginView.as_view(),  name='login'),
    path('', include('django.contrib.auth.urls')),
]