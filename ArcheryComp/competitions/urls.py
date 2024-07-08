from django.urls import path
from competitions import views

app_name = 'competitions'

urlpatterns = [
    path('',              views.IndexView.as_view(),            name='index'),
    path('classical/',    views.ClassicalListView.as_view(),    name='classical_list'),
    path('compound/',     views.CompoundListView.as_view(),     name='compound_list'),
    path('3D/',           views.DListView.as_view(),            name='D_list'),
    path('acheri/',       views.AcheriListView.as_view(),       name='acheri_list'),
    path('asymmetrical/', views.AsymmetricalListView.as_view(), name='asymmetrical_list'),
    path('competition_detail/<int:comp_id>/', views.CompetitionDetailView.as_view(), name='competition_detail'),
]