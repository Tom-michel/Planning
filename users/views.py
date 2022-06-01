from django.shortcuts import render

# Create your views here.



# page d'accueil

def accueil(request):
    return render(request, 'users/accueil.html')


# ensegnant consulter son emploi de temps

def enploiEnseignant(request):

    return render(request, 'users/emploi_enseignant.html')