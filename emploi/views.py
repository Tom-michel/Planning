from django.shortcuts import render
from requests import request
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


# ========================== PAGES DES NON ADMIN DEBUT =======================


# page des enseingnants quand il se connectent pour voir leur emplois de temps

def mon_planning(request):
    
    return render(request, 'emploi/mon_planning.html')


# page des emplois de temps quand un étudiant choisit ses critères

def planning(request):
    
    # obtenir la liste des cours 
    list_cours = []
    list_class = []
    nb = 0

    # liste des specialites
    list_spec = []

    #liste des classe ayant des specialite
    list_class_spec = []
    #liste qui va eliminer les doublons la la liste des specialite
    new_list_spec = []

    # liste qui va eliminer les doublons la la liste des classe
    new_list_class = []

    cours = Cours.objects.all()
    classes = Classes.objects.all()
    specialites = Specialite.objects.all()

    for classe in classes:
        for spec in specialites:
            for cour in cours:
                if spec.classe == cour.classe:
                    list_spec.append(spec)
                    list_class_spec.append(spec.classe)
        for cou in cours:
            if cou.classe == classe:
                list_class.append(classe)
                list_cours.append(cou)


    for s in list_spec:
        if s not in new_list_spec:
            new_list_spec.append(s)

    for i in list_class:
        if i not in new_list_class:
            new_list_class.append(i)
    nb = len(new_list_class)


    context = {
        'specialites': new_list_spec,
        'cours':list_cours,
        'classes': new_list_class,
        'classe_spec': list_class_spec,
        'nb':nb,
        
    }

    return render(request, 'emploi/planning.html', context)

def resultat_recherche(request):

    return render(request, 'emploi/resultat_recherche.html')


# ========================== PAGES DES NON ADMIN FIN =======================




# ========================== DASHBOARD DEBUT =======================


# page d'accueil

def accueil(request):

    search = False
    new_list_class = []

    list_niveau = []
    list_filiere = []
    list_class = []
    list_salle = []
    
    
    list_cours = []
    
    
    classes = Classes.objects.all()
    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()
    cours = Cours.objects.all()
    salles = Salle.objects.all()
    filieres = Filiere.objects.all()
    
    if request.method == "POST":
        search = True

        typeRech = request.POST.get('typeRech')
        if typeRech == "1":
            return planning(request)
        elif typeRech == "2":
            filiere = request.POST.get('filiere2')
            nb = 0
            for cour in cours:
                list_cours.append(cour)
                if cour.classe.filiere.nom_filiere == filiere:
                    list_class.append(cour.classe)
 

            for i in list_class:
                if i not in new_list_class:
                    new_list_class.append(i)
            nb = len(new_list_class)

            context={'search':search, 'classes':new_list_class, 'nb':nb, 'cours':list_cours}

        elif typeRech == "3":
            nb= 0;
            filiere = request.POST.get('filiere3')
            niveau = request.POST.get('niveau1')
            for cour in cours:
                list_cours.append(cour)
                if cour.classe.filiere.nom_filiere == filiere and cour.classe.niveau.nom_niveau == niveau:
                    list_class.append(cour.classe)

            for i in list_class:
                if i not in new_list_class:
                    new_list_class.append(i)
            nb = len(new_list_class)

            context={'search':search, 'classes':new_list_class, 'nb':nb, 'cours':list_cours}

        elif typeRech == "4":
            nb= 0;
            classe = request.POST.get('classe1')
            salle = request.POST.get('salle1')

            for cour in cours:
                list_cours.append(cour)
                if cour.classe.nom_classe == classe and cour.salle.nom_salle == salle:
                    list_class.append(cour.classe)

            for i in list_class:
                if i not in new_list_class:
                    new_list_class.append(i)
            nb = len(new_list_class)

            context={'search':search, 'classes':new_list_class, 'nb':nb, 'cours':list_cours}

        elif typeRech == "5":
            nb= 0;
            filiere = request.POST.get('filiere4')
            niveau = request.POST.get('niveau2')
            classe = request.POST.get('classe2')
            salle = request.POST.get('salle2')
            for cour in cours:
                list_cours.append(cour)
                if cour.classe.filiere.nom_filiere == filiere and cour.classe.niveau.nom_niveau == niveau and cour.salle.nom_salle == salle and cour.classe.nom_classe == classe:
                    list_class.append(cour.classe)

            for i in list_class:
                if i not in new_list_class:
                    new_list_class.append(i)
            nb = len(new_list_class)
            context={'search':search, 'classes':new_list_class, 'nb':nb, 'cours':list_cours}
        
        return  render(request, 'emploi/planning.html', context)
    
    

    for c in cours:
        if c.classe.filiere not in list_filiere:
            list_filiere.append(c.classe.filiere)
        if c.classe.niveau not in list_niveau:
            list_niveau.append(c.classe.niveau)

        if c.salle not in list_salle:
            list_salle.append(c.salle)


        if c.classe not in list_class:
            list_class.append(c.classe)
        

        
        
    context = {
        'classes': list_class,
        'niveaux': list_niveau,
        'salles': list_salle,
        'filieres': list_filiere
    }
    return render(request, 'emploi/accueil.html', context)



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