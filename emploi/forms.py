from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Classe, Cours, Enseignant, Filiere, Niveau, Salle, Specialite, UniteEnseignement


# formulaire pour DJANGO user
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'last_name',
            'password1',
            'password2'
        ]

class UpdateUserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = [
            'username',
            'last_name'
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
            'code',
            'intitule',
            'classe',
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

# classe
class ClasseForm(forms.ModelForm):
    class Meta():
        model = Classe
        fields = [
            'effectif_classe',
            'filiere',
            'niveau',
            'date'
        ]

# cours
class CoursForm(forms.ModelForm):
    class Meta():
        model = Cours
        fields = [
            'jour',
            'type',
            'heure',
            'date',
            'salle',
            'groupe',
            'ue'
        ]

