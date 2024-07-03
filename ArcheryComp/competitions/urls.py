from django.urls import path
from competitions import views

app_name = 'competitions'

urlpatterns = [
    path('', views.index, name='main'),
    path('classical/', views.classical_list, name='classical_list'),
    path('compound/', views.compound_list, name='compound_list'),
    path('3D/', views.D_list, name='D_list'),
    path('acheri/', views.acheri_list, name='acheri_list'),
    path('asymmetrical/', views.asymmetrical_list, name='asymmetrical_list'),
    path('competition_detail/<int:competition_id>/', views.competition_detail, name='competition_detail'),
]