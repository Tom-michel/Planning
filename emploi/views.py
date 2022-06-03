from multiprocessing import context
from django.shortcuts import render

# Create your views here.


# ========================== PAGES DES NON ADMIN DEBUT =======================


# page des enseingnants quand il se connectent pour voir leur emplois de temps

def mon_planning(request):
    return render(request, 'emploi/mon_planning.html')


# page des emplois de temps quand un étudiant choisit ses critères

def planning(request):
    return render(request, 'emploi/planning.html')



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



# ajouter un emploi de temps

def ajout_planning(request, classe):
    context = {'classe':classe}
    return render(request, 'emploi/ajout_planning.html', context)



# modifier un emploi de temps

def modifier_planning(request):
    return render(request, 'emploi/modifier_planning.html')



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

def specialites(request):
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