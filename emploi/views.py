from django.shortcuts import render

# Create your views here.



# page d'accueil du dashboard

def dashboard(request):
    return render(request, 'emploi/dashboard.html')
