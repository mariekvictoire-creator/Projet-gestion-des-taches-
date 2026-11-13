<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======

# Create your views here.
from django.contrib import messages 
from django.db.models import Count, Q 
from django.urls import reverse_lazy 
from django.views.generic import (    
    CreateView,    
    DeleteView,    
    DetailView,    
    ListView,    
    UpdateView, 
    )
from .forms import ProjetForm, TacheForm 
from .models import Projet, Tache

class TacheListView(ListView):    
    """Liste des tâches avec filtres (statut, projet, priorité) et pagination."""    
    model = Tache    
    template_name = "taches/tache_list.html"    
    context_object_name = "taches"    
    paginate_by = 10    
    def get_queryset(self):        
        qs = Tache.objects.select_related("projet")        
        statut = self.request.GET.get("statut", "")        
        projet = self.request.GET.get("projet", "")        
        priorite = self.request.GET.get("priorite", "")        
        if statut in Tache.Statut.values:            
            qs = qs.filter(statut=statut)        
            if priorite in Tache.Priorite.values:            
                qs = qs.filter(priorite=priorite)        
                if projet.isdigit():            
                    qs = qs.filter(projet_id=int(projet))        
                    return qs    
def get_context_data(self, **kwargs):        
    ctx = super().get_context_data(**kwargs)        
    params = self.request.GET.copy()        
    params.pop("page", None)        
    ctx.update(            
        statuts=Tache.Statut.choices,            
        priorites=Tache.Priorite.choices,            
        projets=Projet.objects.all(),            
        statut_courant=self.request.GET.get("statut", ""),            
        projet_courant=self.request.GET.get("projet", ""),            
        priorite_courante=self.request.GET.get("priorite", ""),            
        querystring=params.urlencode(),        
        )        
    return ctx 

class TacheDetailView(DetailView):    
    model = Tache    
    template_name = "taches/tache_detail.html" 

class TacheCreateView(CreateView):    
    model = Tache    
    form_class = TacheForm    
    template_name = "taches/tache_form.html" 

    def get_initial(self):        
        initial = super().get_initial()        
        projet = self.request.GET.get("projet", "")        
        if projet.isdigit():            
            initial["projet"] = int(projet)        
            return initial    
        
    def form_valid(self, form):        
        messages.success(self.request, "Tâche créée avec succès.")        
        return super().form_valid(form)
        
    def get_success_url(self):        
        return reverse_lazy("taches:projet_detail", kwargs={"pk": self.object.projet_id}) 
    
class TacheUpdateView(UpdateView):    
    model = Tache    
    form_class = TacheForm    
    template_name = "taches/tache_form.html"    
    def form_valid(self, form):        
        messages.success(self.request, "Tâche modifiée avec succès.")        
        return super().form_valid(form)  
      
    def get_success_url(self):
        return reverse_lazy("taches:tache_detail", kwargs={"pk": self.object.pk})
    
    class TacheDeleteView(DeleteView):    
        model = Tache    
        template_name = "taches/confirm_delete.html"    
        success_url = reverse_lazy("taches:tache_liste")    

        def form_valid(self, form):        
            messages.success(self.request, "Tâche supprimée.")        
            return super().form_valid(form)    
        def get_context_data(self, **kwargs):        
            ctx = super().get_context_data(**kwargs)        
            ctx["libelle"] = f"la tâche « {self.object.titre} »"        
            ctx["annuler_url"] = reverse_lazy("taches:tache_detail", kwargs={"pk": self.object.pk})        
            return ctx

class ProjetListView(ListView):    
    model = Projet    
    template_name = "taches/projet_list.html"    
    context_object_name = "projets"    

    def get_queryset(self):        
        return Projet.objects.annotate(            
            nb_taches=Count("taches"),            
            nb_terminees=Count("taches", filter=Q(taches__statut=Tache.Statut.TERMINEE)),        
            ) 

class ProjetDetailView(DetailView):    
    """Détail d'un projet = liste de ses tâches (filtrable par statut)."""    
    model = Projet    
    template_name = "taches/projet_detail.html" 

    def get_context_data(self, **kwargs):        
        ctx = super().get_context_data(**kwargs)        
        statut = self.request.GET.get("statut", "")        
        taches = self.object.taches.all()        
        if statut in Tache.Statut.values:            
            taches = taches.filter(statut=statut)        
            ctx.update(            
                taches=taches,            
                statuts=Tache.Statut.choices,            
                statut_courant=statut,        
                )        
            return ctx 
        
class ProjetCreateView(CreateView):    
    model = Projet    
    form_class = ProjetForm    
    template_name = "taches/projet_form.html"    
    success_url = reverse_lazy("taches:projet_liste")    
    def form_valid(self, form):        
        messages.success(self.request, "Projet créé avec succès.")        
        return super().form_valid(form) 
    
class ProjetUpdateView(UpdateView):    
    model = Projet    
    form_class = ProjetForm    
    template_name = "taches/projet_form.html"    
    success_url = reverse_lazy("taches:projet_liste")  

    def form_valid(self, form):        
        messages.success(self.request, "Projet modifié avec succès.")        
        return super().form_valid(form)
    
class ProjetDeleteView(DeleteView):    
    model = Projet    
    template_name = "taches/confirm_delete.html"
    success_url = reverse_lazy("taches:projet_liste")    

    def form_valid(self, form):        
        messages.success(self.request, "Projet et ses tâches supprimés.")        
        return super().form_valid(form)    
    
    def get_context_data(self, **kwargs):        
        ctx = super().get_context_data(**kwargs)        
        ctx["libelle"] = f"le projet « {self.object.nom} »"        
        ctx["avertissement"] = (            
            f"Attention : les {self.object.taches.count()} tâche(s) de ce projet seront aussi supprimées.    "        
            )        
        ctx["annuler_url"] = reverse_lazy("taches:projet_liste")        
        return ctx
>>>>>>> feature/gestion-taches
