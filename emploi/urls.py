from django.urls import path
from .views import *

urlpatterns = [

    # ======= PAGES VISIBLES AUX UTILISATEURS ====
    path('', accueil, name="accueil"),
    path('mon_planning', mon_planning, name="mon_planning"),
    path('planning', planning, name="planning"),


    # ======= PAGES DU DASBOARD =================
    path('dashboard/', dashboard, name="dashboard"),
    path('ajout_planning/<str:id_clas>', ajout_planning, name="ajout_planning"),
    path('modifier_planning/', modifier_planning, name="modifier_planning"),
    path('enseignant/', enseignant, name="enseignant"),
    path('edit_enseignant/<str:id_e>', edit_enseignant, name="edit_enseignant"),
    path('supp_enseignant/<str:id_e>', supp_enseignant, name="supp_enseignant"),
    path('unite_enseignements/', unite_enseignements, name="unite_enseignements"),
    path('unite_enseignements/', unite_enseignements, name="unite_enseignements"),
    path('filieres/', filieres, name="filieres"),
    path('specialites/', specialites, name="specialites"),
    path('niveaux/', niveaux, name="niveaux"),
    path('salles/', salles, name="salles"),
    path('classes/', classes, name="classes"),
    path('user_logout/', user_logout, name="user_logout"),
]
