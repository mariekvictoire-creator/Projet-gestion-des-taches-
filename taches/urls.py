from django.urls import path 
from . import views 
app_name = "taches" 
urlpatterns = [    # Tâches    
    path("", views.TacheListView.as_view(), name="tache_liste"),    
    path("taches/nouvelle/", views.TacheCreateView.as_view(), name="tache_creer"),    
    path("taches/<int:pk>/", views.TacheDetailView.as_view(), name="tache_detail"),    
    path("taches/<int:pk>/modifier/", views.TacheUpdateView.as_view(), name="tache_modifier"),    
    path("taches/<int:pk>/supprimer/", views.TacheDeleteView.as_view(), name="tache_supprimer"),    
    # Projets  
    path("projets/", views.ProjetListView.as_view(), name="projet_liste"),    
    path("projets/nouveau/", views.ProjetCreateView.as_view(), name="projet_creer"),    
    path("projets/<int:pk>/", views.ProjetDetailView.as_view(), name="projet_detail"),    
    path("projets/<int:pk>/modifier/", views.ProjetUpdateView.as_view(), name="projet_modifier"),    
    path("projets/<int:pk>/supprimer/", views.ProjetDeleteView.as_view(), name="projet_supprimer"), 
    ]