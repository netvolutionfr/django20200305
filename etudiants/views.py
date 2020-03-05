from datetime import datetime

from django.shortcuts import render

# Create your views here.


def date_actuelle(request):
    return render(request, 'etudiants/date.html',
                  {'date': datetime.now})

