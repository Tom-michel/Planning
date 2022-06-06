from operator import mod
from re import M
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Enseignant(models.Model):
	telephone = models.CharField(max_length=14)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="enseignant")
    
 
 
class UniteEnseignement(models.Model):
    
    nom_ue = models.CharField(max_length=40)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom_ue
    
    

class  Filiere(models.Model):
    nom_filiere = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nom_filiere
    
    
class Niveau(models.Model):
    nom_niveau = models.CharField(max_length=10)
    
    def __str__(self) :
        return self.nom_niveau
    

class Groupe(models.Model):
    
    nom_groupe = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nom_groupe
    

class Classes(models.Model):
    
    effectif_classe = models.IntegerField('Effectif')
    
    nom_classe = models.CharField(max_length=20)
    
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom_classe
    


class Specialite(models.Model):
    
    nom_specialite = models.CharField(max_length=30)
    
    classe = models.ForeignKey(Classes, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom_specialite


 
class Salle(models.Model):
    nom_salle = models.CharField(max_length=50, blank=True)
    capacite_salle = models.IntegerField('capacite')

    def __str__(self):
        return self.nom_salle
    
class Cours(models.Model):

    JOURS = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    ]

    HEURE = [
            ('7h-9h55', '7h-9h55'),
            ('10h05-12h55', '10h05-12h55'),
            ('13h05-15h55', '13h05-15h55'),
            ('16h05-18h55', '16h05-18h55'),
            ('19h05-21h55', '19h05-21h55'),

    ]

    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    
    classe = models.ForeignKey(Classes, on_delete=models.CASCADE)
    
    ue = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE)
    
    jour = models.CharField(max_length=20, choices=JOURS, default="Lundi", blank=True)
    heure = models.CharField(max_length=12, choices=HEURE, default="7h-9h55", blank=True)
    
    
    def __str__(self):
        return self.ue.nom_ue
    



    