from django import forms 
from .models import Projet, Tache 


class BootstrapMixin:    
    """Ajoute les classes Bootstrap à tous les champs."""    

    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)        
        for champ in self.fields.values():            
            css = "form-select" if isinstance(champ.widget, forms.Select) else "form-control"
            champ.widget.attrs["class"] = css
                
class ProjetForm(BootstrapMixin, forms.ModelForm):    
    class Meta:        
        model = Projet        
        fields = ["nom", "description"]        
        widgets = {"description": forms.Textarea(attrs={"rows": 4})} 
        
class TacheForm(BootstrapMixin, forms.ModelForm):    
    class Meta:        
        model = Tache        
        fields = ["titre", "description", "statut", "priorite", "projet"]        
        widgets = {"description": forms.Textarea(attrs={"rows": 4})}