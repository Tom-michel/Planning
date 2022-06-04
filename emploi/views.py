from django.shortcuts import render
from requests import request
from .models import *
from django.contrib.auth.models import User

# Create your views here.


# ========================== PAGES DES NON ADMIN DEBUT =======================


# page des enseingnants quand il se connectent pour voir leur emplois de temps

def mon_planning(request):
    
    
    return render(request, 'emploi/mon_planning.html')


# page des emplois de temps quand un étudiant choisit ses critères

def planning(request):
    
     
    list_class = []
    liste_ue = []
    list_filiere = []
    list_niveau = []
    list_ens = []
    list_cours = []
    list_salle = []
    list_specialite = []
    list_group = []
    list_fil = []
    
    
    classes = Classes.objects.all()
    ues = UniteEnseignement.objects.all()
    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()
    enseignants = Enseignant.objects.all()
    cours = Cours.objects.all()
    salles = Salle.objects.all()
    specialite = Specialite.objects.all()
    groupes = Groupe.objects.all()
    filieres = Filiere.objects.all()
    
    
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
        
    for fil in filieres:
        list_fil.append(fil)
        
        
    context = {
        'cours':list_cours,
        'classes': list_class,
        'ues': liste_ue,
        'enseignants': list_ens,
        'niveaux': list_niveau,
        'salles': list_salle,
        'specialites': list_specialite,
        'groupes': list_group,
        'filieres': list_fil
    }

    return render(request, 'emploi/planning.html', context)




# ========================== PAGES DES NON ADMIN FIN =======================




# ========================== DASHBOARD DEBUT =======================


# page d'accueil

def accueil(request):
    return render(request, 'emploi/accueil.html')



# page d'accueil du dashboard

def dashboard(request):
    
    if request.method == 'POST':
        classe = request.POST.get('classe')
        # context = {'classe':classe}
        # return render(request, 'emploi/ajout_planning.html', context)
        msg = "salut"
        return ajout_planning(request, classe)

    return render(request, 'emploi/dashboard.html')

def ajout_planning(request, classe):
    context = {'classe':classe}
    return render(request, 'emploi/ajout_planning.html', context)

# page d'accueil des enseignants sur le dashbord

def enseignant(request):
    return render(request, 'emploi/enseignants.html')



# page d'accueil de UEs

def unite_enseignements(request):
    return render(request, 'emploi/ue.html')



# page d'accueil des filieres

def filieres(request):
    return render(request, 'emploi/filieres.html')



# page d'accueil des specialites

def specialite(request):
    return render(request, 'emploi/specialite.html')



# page d'accueil des niveaux

def niveaux(request):
    return render(request, 'emploi/niveaux.html')



# page d'accueil des salles

def salles(request):
    return render(request, 'emploi/salles.html')



# page d'accueil des classes

def classes(request):
    return render(request, 'emploi/classes.html')



# page d'accueil des groupes

def groupes(request):
    return render(request, 'emploi/groupes.html')


# ========================== DASHBOARD FIN =======================