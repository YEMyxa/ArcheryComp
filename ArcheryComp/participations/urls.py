from django.urls import path, include
from participations import views

app_name = 'participations'

urlpatterns = [
    path('', views.SportsmanListView.as_view(), name='sportsmans_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<str:username>/', include([
        path('participations_list/', views.PersonalParticipationListView.as_view(), name='participations_list'),
        path('team_participations_list/', views.TeamParticipationListView.as_view(), name='team_participations_list'),
        path('mixed_participations_list/', views.MixedParticipationListView.as_view(), name='mixed_participations_list'),
    ])),
    path('<str:username>', views.UserParticipitionsView.as_view(), name='user_part')
]