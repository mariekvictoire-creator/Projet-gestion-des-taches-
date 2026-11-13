<<<<<<< HEAD
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
=======
from django.db import models 


class Projet(models.Model):    
    nom = models.CharField("Nom", max_length=150, unique=True)    
    description = models.TextField("Description", blank=True)    
    date_creation = models.DateTimeField("Créé le", auto_now_add=True)    
    

    class Meta:        
        ordering = ["nom"]    

    def __str__(self):        
        return self.nom 
    

class Tache(models.Model):   

    class Statut(models.TextChoices):        
        A_FAIRE = "A_FAIRE", "À faire"        
        EN_COURS = "EN_COURS", "En cours"        
        TERMINEE = "TERMINEE", "Terminée"    
    
    class Priorite(models.TextChoices):        
        BASSE = "BASSE", "Basse"        
        MOYENNE = "MOYENNE", "Moyenne"
        HAUTE = "HAUTE", "Haute"    
        titre = models.CharField("Titre", max_length=200)    
        description = models.TextField("Description", blank=True)    
    statut = models.CharField(        
        "Statut", max_length=10, 
        choices=Statut.choices, 
        default=Statut.A_FAIRE    
        )    
    priorite = models.CharField(        
        "Priorité", max_length=10, 
        choices=Priorite.choices, 
        default=Priorite.MOYENNE    
        )    
    projet = models.ForeignKey(        
        Projet,        
        verbose_name="Projet",        
        on_delete=models.CASCADE,        
        related_name="taches",    
        )    
    date_creation = models.DateTimeField("Créée le", auto_now_add=True)    
    date_modification = models.DateTimeField("Modifiée le", auto_now=True)    
    
    class Meta:        
        ordering = ["-date_creation"]        
        verbose_name = "tâche"        
        verbose_name_plural = "tâches"    
        def __str__(self):        
            return self.titre    
        @property    
        def badge_statut(self):        
            return {            
                self.Statut.A_FAIRE: "secondary",            
                self.Statut.EN_COURS: "primary",            
                self.Statut.TERMINEE: "success",        
                }.get(self.statut, "secondary") 
           
        @property    
        def badge_priorite(self):        
            return {            
                self.Priorite.BASSE: "info",            
                self.Priorite.MOYENNE: "warning",            
                self.Priorite.HAUTE: "danger",        
                }.get(self.priorite, "secondary")
>>>>>>> feature/gestion-taches
