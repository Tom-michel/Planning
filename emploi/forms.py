from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Enseignant, Filiere, Niveau, Salle, Specialite, UniteEnseignement


# formulaire pour DJANGO user
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]

class UpdateUserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = [
            'username'
        ]


# formulaire pour Enseignant
class EnsForm(forms.ModelForm):

    class Meta():
        model = Enseignant
        fields = [
            'matricule',
            'date'
        ]

# UE
class UeForm(forms.ModelForm):

    class Meta():
        model = UniteEnseignement
        fields = [
            'intitule',
            'enseignant',
            'date'
        ]

# filiere
class FilereForm(forms.ModelForm):
    class Meta():
        model = Filiere
        fields = [
            'nom_filiere'
        ]

# specialités
class SpeForm(forms.ModelForm):
    class Meta():
        model = Specialite
        fields = [
            'nom_specialite',
            'classe',
            'date'
        ]

# niveaux
class NiveauForm(forms.ModelForm):
    class Meta():
        model = Niveau
        fields = [
            'nom_niveau',
            'date'
        ]

# salles
class SalleForm(forms.ModelForm):
    class Meta():
        model = Salle
        fields = [
            'nom_salle',
            'capacite_salle',
            'date'
        ]


