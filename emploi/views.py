from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

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