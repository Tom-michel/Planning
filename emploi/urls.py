from django.urls import path
from .views import *

urlpatterns = [

    # ======= PAGES VISIBLES AUX UTILISATEURS ====
    path('', accueil, name="accueil"),
    path('mon_planning', mon_planning, name="mon_planning"),
    path('planning', planning, name="planning"),
    path('resulta', resultat_recherche, name="resultat"),


    # ======= PAGES DU DASBOARD =================
    path('dasboard/', dashboard, name="dashboard"),
    path('ajout_planning/', ajout_planning, name="ajout_planning"),
    path('unite_enseignements/', unite_enseignements, name="unite_enseignements"),
    path('unite_enseignements/', unite_enseignements, name="unite_enseignements"),
    path('filieres/', filieres, name="filieres"),
    path('specialite/', specialite, name="specialite"),
    path('niveaux/', niveaux, name="niveaux"),
    path('salles/', salles, name="salles"),
    path('classes/', classes, name="classes"),
    path('groupes/', groupes, name="groupes"),
    path('unite_enseignements/', unite_enseignements, name="unite_enseignements"),
    path('unite_enseignements/', unite_enseignements, name="unite_enseignements"),
    path('unite_enseignements/', unite_enseignements, name="unite_enseignements"),
]
