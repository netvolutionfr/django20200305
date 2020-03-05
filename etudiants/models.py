from django.db import models

# Create your models here.
from django.utils import timezone


class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(default=timezone.now)

