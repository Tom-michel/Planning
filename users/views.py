from django.shortcuts import render
from emploi.models import *


# Create your views here.



# page d'accueil

def accueil(request):
    return render(request, 'users/accueil.html')


# ensegnant consulter son emploi de temps

def enploiEnseignant(request):
    
    list_class = []
    liste_ue = []
    list_filiere = []
    list_niveau = []
    list_ens = []
    list_cours = []
    list_salle = []
    list_specialite = []
    list_group = []
    
    
    classes = Classes.objects.all()
    ues = UniteEnseignement.objects.all()
    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()
    enseignants = Enseignant.objects.all()
    cours = Cours.objects.all()
    salles = Salle.objects.all()
    specialite = Specialite.objects.all()
    groupes = Groupe.objects.all()
    
    
    for cour in cours:
        list_cours.append(cour)
        
    for classe in classes:
        list_class.append(classe)
        
    for ue in ues:
        liste_ue.append(ue)
        
    for ens in enseignants:
        list_ens.append(ens)
        
    for niv in niveaux:
        list_niveau.append(niv)
    
    for sal in salles:
        list_salle.append(sal)
        
    for spec in specialite:
        list_specialite.append(spec)
        
    for group in groupes:
        list_group.append(group)
        
        
    context = {
        'cours':list_cours,
        'classes': list_class,
        'ues': liste_ue,
        'enseignants': list_ens,
        'niveaux': list_niveau,
        'salles': list_salle,
        'specialites': list_specialite,
        'groupes': list_group
    }

    return render(request, 'recherche.html', context)

