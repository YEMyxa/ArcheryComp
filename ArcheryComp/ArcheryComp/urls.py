from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('competitions.urls', namespace='competitions')),
    path('participations/', include('participations.urls', namespace='participations')),
    path('users/', include('users.urls')),
]
