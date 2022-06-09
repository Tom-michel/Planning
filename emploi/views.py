from django.http import HttpResponseRedirect
from django.shortcuts import render
from requests import request
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *


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
    classes = Classe.objects.all()
    specialites = Specialite.objects.all()

    for classe in classes:
        for spec in specialites:
            for cour in cours:
                if spec.classe == cour.ue.classe:
                    list_spec.append(spec)
                    list_class_spec.append(spec.classe)
        for cou in cours:
            if cou.ue.classe == classe:
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
    
    
    classes = Classe.objects.all()
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
                if cour.ue.classe.filiere.nom_filiere == filiere:
                    list_class.append(cour.ue.classe)
 

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
                if cour.ue.classe.filiere.nom_filiere == filiere and cour.ue.classe.niveau.nom_niveau == niveau:
                    list_class.append(cour.ue.classe)

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
                if cour.ue.classe.nom_classe == classe and cour.salle.nom_salle == salle:
                    list_class.append(cour.ue.classe)

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
                if cour.ue.classe.filiere.nom_filiere == filiere and cour.ue.classe.niveau.nom_niveau == niveau and cour.salle.nom_salle == salle and cour.ue.classe.nom_classe == classe:
                    list_class.append(cour.ue.classe)

            for i in list_class:
                if i not in new_list_class:
                    new_list_class.append(i)
            nb = len(new_list_class)
            context={'search':search, 'classes':new_list_class, 'nb':nb, 'cours':list_cours}
        
        return  render(request, 'emploi/planning.html', context)
    
    

    for c in cours:
        if c.ue.classe.filiere not in list_filiere:
            list_filiere.append(c.ue.classe.filiere)
        if c.ue.classe.niveau not in list_niveau:
            list_niveau.append(c.ue.classe.niveau)

        if c.salle not in list_salle:
            list_salle.append(c.salle)


        if c.ue.classe not in list_class:
            list_class.append(c.ue.classe)
        

        
        
    context = {
        'classes': list_class,
        'niveaux': list_niveau,
        'salles': list_salle,
        'filieres': list_filiere
    }
    return render(request, 'emploi/accueil.html', context)



# page d'accueil du dashboard

def dashboard(request):
    classeList = Classe.objects.all()
    if request.method == 'POST':
        classe = request.POST.get('classe')
        return ajout_planning(request, classe)
    context = {'classeList':classeList}
    return render(request, 'emploi/dashboard.html', context)



# ajouter un emploi de temps

def ajout_planning(request, id_clas):
    classeList = Classe.objects.all()
    coursList = Cours.objects.all()
    cours_form = CoursForm()
    classe = Classe.objects.get(id=id_clas)
    ueList = UniteEnseignement.objects.all()
    
    if request.method == 'POST':
        cours_form = CoursForm(data=request.POST)
        if cours_form.is_valid():
            cours = cours_form.save()
            cours.save()
            # return HttpResponseRedirect('ajout_planning')
        else:
            err = cours_form.errors
            context = {
                'coursList':coursList,
                'cours_form':cours_form,
                'classeList':classeList,
                'ueList':ueList,
                'classe':classe,
                'err':err
            }
            return render(request, 'emploi/ajout_planning.html', context)
    context = {
        'coursList':coursList,
        'cours_form':cours_form,
        'classeList':classeList,
        'ueList':ueList,
        'classe':classe
    }
    return render(request, 'emploi/ajout_planning.html', context)



# modifier un emploi de temps

def modifier_planning(request):
    return render(request, 'emploi/modifier_planning.html')




# ============================ LES TABLES ==========================

    return render(request, 'emploi/dashboard.html')

def ajout_planning(request, classe):
    context = {'classe':classe}
    return render(request, 'emploi/ajout_planning.html', context)

# page d'accueil des enseignants sur le dashbord

def enseignant(request):
    ensList = Enseignant.objects.all()
    ens_form = EnsForm()
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        ens_form = EnsForm(data=request.POST)
        if user_form.is_valid() and ens_form.is_valid():
            user = user_form.save()
            user.save()
            ens = ens_form.save(commit=False)
            ens.user = user
            ens.save()
            ensList = Enseignant.objects.all()
            return HttpResponseRedirect('../enseignant')
        else:
            err1 = user_form.errors
            err2 = ens_form.errors
            context = {'ens_form':ens_form, 'user_form':user_form, 'ensList':ensList, 'err1':err1, 'err2':err2}
            return render(request, 'emploi/enseignants.html', context)
    else:        
        context = {'ens_form':ens_form, 'user_form':user_form, 'ensList':ensList}
        return render(request, 'emploi/enseignants.html', context)



# modifier un enseignant

def edit_enseignant(request, id_e):
    ens = Enseignant.objects.get(id=id_e)
    ens_form = EnsForm(instance=ens)
    user_form = UpdateUserForm(instance=ens.user)
    if request.method == 'POST':
        ens_form = EnsForm(data=request.POST, instance=ens)
        user_form = UpdateUserForm(data=request.POST, instance=ens.user)
        if user_form.is_valid() and ens_form.is_valid():
            user = user_form.save()
            user.save()
            ens = ens_form.save(commit=False)
            ens.user = user
            ens.save()
            return HttpResponseRedirect('../enseignant')
        else:
            err1 = user_form.errors
            err2 = ens_form.errors
            context = {'ens_form':ens_form, 'user_form':user_form, 'err1':err1, 'err2':err2}
            return render(request, 'emploi/edit_enseignant.html', context)
    context = {'ens_form':ens_form, 'user_form':user_form}
    return render(request, 'emploi/edit_enseignant.html', context)


# supprimer un enseignant

def supp_enseignant(request, id_e):
    ens = Enseignant.objects.get(id=id_e)
    user = User.objects.get(id=ens.user.id)
    if request.method == 'POST':
        user.delete()
        ens.delete()
        return HttpResponseRedirect('../../enseignant')
    context = {'ens':ens}
    return render(request, 'emploi/supp_enseignant.html', context)



# page d'accueil de UEs

def unite_enseignements(request):
    ueList = UniteEnseignement.objects.all()
    ue_form = UeForm()
    if request.method == 'POST':
        ue_form = UeForm(data=request.POST)
        if ue_form.is_valid():
            ue = ue_form.save()
            ue.save()
            return HttpResponseRedirect('../unite_enseignements')
    context = {
        'ueList':ueList, 'ue_form':ue_form
    }        
    return render(request, 'emploi/ue.html', context)



# page d'accueil des filieres

def filieres(request):
    filList = Filiere.objects.all()
    fil_form = FilereForm()
    if request.method == 'POST':
        fil_form = FilereForm(data=request.POST)
        if fil_form.is_valid():
            fil = fil_form.save()
            fil.save()
            return HttpResponseRedirect('../filieres')
    context = {
        'filList':filList, 'fil_form':fil_form
    }        
    return render(request, 'emploi/filieres.html', context)



# page d'accueil des specialites

def specialites(request):
    speList = Specialite.objects.all()
    spe_form = SpeForm()
    if request.method == 'POST':
        spe_form = SpeForm(data=request.POST)
        if spe_form.is_valid():
            spe = spe_form.save()
            spe.save()
            return HttpResponseRedirect('../specialites')
    context = {
        'speList':speList, 'spe_form':spe_form
    }        
    return render(request, 'emploi/specialite.html', context)



# page d'accueil des niveaux

def niveaux(request):
    nivList = Niveau.objects.all()
    niv_form = NiveauForm()
    if request.method == 'POST':
        niv_form = NiveauForm(data=request.POST)
        if niv_form.is_valid():
            niv = niv_form.save()
            niv.save()
            return HttpResponseRedirect('../niveaux')
    context = {
        'nivList':nivList, 'niv_form':niv_form
    }        
    return render(request, 'emploi/niveaux.html', context)



# page d'accueil des salles

def salles(request):
    salList = Salle.objects.all()
    sal_form = SalleForm()
    if request.method == 'POST':
        sal_form = SalleForm(data=request.POST)
        if sal_form.is_valid():
            sal = sal_form.save()
            sal.save()
            return HttpResponseRedirect('../salles')
    context = {
        'salList':salList, 'sal_form':sal_form
    }        
    return render(request, 'emploi/salles.html', context)



# page d'accueil des classes

def classes(request):
    classeList = Classe.objects.all()
    classe_form = ClasseForm()
    if request.method == 'POST':
        classe_form = ClasseForm(data=request.POST)
        if classe_form.is_valid():
            classe = classe_form.save()
            classe.save()
            return HttpResponseRedirect('../classes')
    context = {
        'classeList':classeList, 'classe_form':classe_form
    }        
    return render(request, 'emploi/classes.html', context)



# @login_required(login_url='connexion')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# ========================== DASHBOARD FIN =======================