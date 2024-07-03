from django.http import HttpResponse
from django.urls import reverse

def index(request):
    participation_list = ''
    paricipations_amount = 3
    for i in range(paricipations_amount):
        participation_url = reverse('competitions:competition_detail', kwargs={'competition_id': i})
        participation_list += (f"Результаты участия {(i+1)}</br>"
                               f"<a href='{participation_url}'>Соревнование {(i+1)}</a><br/>")
    html = (f"<h1>Список участий</h1>"
            + participation_list)
    return HttpResponse(html)