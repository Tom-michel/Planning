from django.urls import path
from .views import *

urlpatterns = [

    # ======= PAGES VISIBLES AUX UTILISATEURS ====
    path('', accueil, name="accueil"),
    path('mon_planning', mon_planning, name="mon_planning"),
    path('planning', planning, name="planning"),


    # ======= PAGES DU DASBOARD =================
    path('dashboard/', dashboard, name="dashboard"),
    path('enseignant/', enseignant, name="enseignant"),
    path('unite_enseignements/', unite_enseignements, name="unite_enseignements"),
    path('unite_enseignements/', unite_enseignements, name="unite_enseignements"),
    path('filieres/', filieres, name="filieres"),
    path('specialites/', specialites, name="specialites"),
    path('niveaux/', niveaux, name="niveaux"),
    path('salles/', salles, name="salles"),
    path('classes/', classes, name="classes"),
    path('groupes/', groupes, name="groupes"),
]
