from django.urls import path
from .views import *

urlpatterns = [
    path('', accueil, name="accueil"),

    path('enseignant/emploi_de_temps', enploiEnseignant, name='TimeTable')
]
