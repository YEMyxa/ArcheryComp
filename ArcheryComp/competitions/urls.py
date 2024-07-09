from django.urls import path, include
from competitions import views
from participations import views as views_p

app_name = 'competitions'

urlpatterns = [
    path('',              views.IndexView.as_view(),            name='index'),
    path('classical/',    views.ClassicalListView.as_view(),    name='classical_list'),
    path('compound/',     views.CompoundListView.as_view(),     name='compound_list'),
    path('3D/',           views.DListView.as_view(),            name='D_list'),
    path('acheri/',       views.AcheriListView.as_view(),       name='acheri_list'),
    path('asymmetrical/', views.AsymmetricalListView.as_view(), name='asymmetrical_list'),
    path('competition_detail/<int:comp_id>/', include([
        path('', views.CompetitionDetailView.as_view(), name='competition_detail'),
        path('personal_program/', views_p.PersonalProgramCreateView.as_view(), name='personal_program'),
        path('team_program/', views_p.TeamProgramCreateView.as_view(), name='team_program'),
        path('mixed_program/', views_p.MixedProgramCreateView.as_view(), name='mixed_program'),
        path('/<int:program_id>/', include([
            path('add_personal/', views_p.PersonalParticipationCreateView.as_view(), name='add_personal'),
            path('add_team/',     views_p.TeamParticipationCreateView.as_view(),     name='add_team'),
            path('add_mixed/',    views_p.MixedParticipationCreateView.as_view(),    name='add_mixed'),
            ])),
        path('/<int:participation_id>/', include([
            path('update_personal/', views_p.PersonalParticipationUpdateView.as_view(), name='update_personal'),
            path('update_team/',     views_p.TeamParticipationUpdateView.as_view(),     name='update_team'),
            path('update_mixed/',    views_p.MixedParticipationUpdateView.as_view(),    name='update_mixed'),
        ])),
        path('update_program/', views.ProgramUpdateView.as_view(),name='update_program')
    ])),
]