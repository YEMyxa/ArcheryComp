from django.urls import path
from participations import views

app_name = 'participations'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:username>', views.UserParticipitionsView.as_view(), name='user_part')
]