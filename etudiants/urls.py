from django.urls import path

from etudiants import views

urlpatterns = [
    path('date', views.date_actuelle, name="date")

]
