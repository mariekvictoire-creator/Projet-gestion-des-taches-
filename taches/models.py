from django.db import models
from django.contrib.auth.models import User

class Tache(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titre