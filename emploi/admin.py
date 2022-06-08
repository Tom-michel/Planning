from django.contrib import admin
from .models import *

# Register your models here.

class AdminEnseignant(admin.ModelAdmin):
    list_display = ['user', 'matricule']
    
class AdminUe(admin.ModelAdmin):
    list_display = ['code_ue', 'intitule', 'enseignant']
    
class AdminCours(admin.ModelAdmin):
    list_display = ['ue', 'salle', 'groupe', 'jour', 'heure']
    list_filter = ['salle']
    
class AdminClasse(admin.ModelAdmin):
    list_display = ['nom_classe', 'effectif_classe', 'niveau', 'filiere']
    list_filter = ['nom_classe', 'niveau']
    
class AdminFiliere(admin.ModelAdmin):
    list_display = ['nom_filiere', 'date']
    
class AdminNiveau(admin.ModelAdmin):
    list_display = ['nom_niveau', 'date']

    
class AdminSalle(admin.ModelAdmin):
    
    list_display = ['nom_salle', 'capacite_salle', 'date']
    list_filter = ['capacite_salle']
    
class AdminSpecilite(admin.ModelAdmin):
    list_display = ['nom_specialite', 'classe']
    list_filter = ['classe']



admin.site.register(Enseignant, AdminEnseignant)
admin.site.register(UniteEnseignement, AdminUe)
admin.site.register(Classe, AdminClasse)
admin.site.register(Cours, AdminCours)
admin.site.register(Filiere, AdminFiliere)
admin.site.register(Niveau, AdminNiveau)
admin.site.register(Salle, AdminSalle)
admin.site.register(Specialite, AdminSpecilite)
