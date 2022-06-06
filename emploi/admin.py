from django.contrib import admin
from .models import *

# Register your models here.

class AdminEnseignant(admin.ModelAdmin):
    list_display = ['user', 'telephone']
    
class AdminUe(admin.ModelAdmin):
    list_display = ['nom_ue', 'intitule', 'enseignant']
    
class AdminCours(admin.ModelAdmin):
    list_display = ['classe','ue', 'salle', 'groupe', 'jour', 'heure']
    list_filter = ['classe']
    
class AdminClasse(admin.ModelAdmin):
    list_display = ['nom_classe', 'effectif_classe']
    list_filter = ['nom_classe']
    
class AdminFiliere(admin.ModelAdmin):
    list_display = ['nom_filiere']
    
class AdminNiveau(admin.ModelAdmin):
    list_display = ['nom_niveau']

class AdminGroupe(admin.ModelAdmin):
    list_display = ['nom_groupe']
    
class AdminSalle(admin.ModelAdmin):
    
    list_display = ['nom_salle', 'capacite_salle']
    
class AdminSpecilite(admin.ModelAdmin):
    list_display = ['nom_specialite', 'classe']



admin.site.register(Enseignant, AdminEnseignant)
admin.site.register(UniteEnseignement, AdminUe)
admin.site.register(Classes, AdminClasse)
admin.site.register(Cours, AdminCours)
admin.site.register(Filiere, AdminFiliere)
admin.site.register(Niveau, AdminNiveau)
admin.site.register(Salle, AdminSalle)
admin.site.register(Groupe, AdminGroupe)
admin.site.register(Specialite, AdminSpecilite)
