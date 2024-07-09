from django.urls import path
from participations import views

app_name = 'participations'

urlpatterns = [
    path('', views.SportsmanListView.as_view(), name='sportsmans_list'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('<int:id>/participations_list/', views.PersonalParticipationListView.as_view(), name='participations_list'),
]