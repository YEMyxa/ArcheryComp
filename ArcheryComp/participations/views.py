from django.http import HttpResponse
from django.urls import reverse

def index(request):
    html = f"<h1>Список участий</h1>"
    return HttpResponse(html)