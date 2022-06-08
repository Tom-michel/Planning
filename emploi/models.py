from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


    
 
class Enseignant(models.Model):
    matricule = models.CharField(max_length=7, unique=True)
    date = models.DateField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='enseignant')
    def __str__(self):
        return f'{self.user.username}'   
    

class  Filiere(models.Model):
    nom_filiere = models.CharField(max_length=30, unique=True)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nom_filiere
    
    
class Niveau(models.Model):
    nom_niveau = models.CharField(max_length=10, unique=True)
    date = models.DateField(default=timezone.now)
    
    def __str__(self) :
        return self.nom_niveau
    
    

class Classe(models.Model):
    nom_classe = models.CharField(max_length=20, blank=True)
    effectif_classe = models.IntegerField('Effectif')
    date = models.DateField(default=timezone.now)  
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom_classe
    


class Specialite(models.Model):
    nom_specialite = models.CharField(max_length=30, unique=True)
    date = models.DateField(default=timezone.now)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.classe}-{self.nom_specialite}-{self.nom_specialite}'


 
class Salle(models.Model):
    nom_salle = models.CharField(max_length=50, unique=True)
    capacite_salle = models.IntegerField('capacite')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nom_salle


 
class UniteEnseignement(models.Model):
    code_ue = models.CharField(max_length=200, unique=True)
    intitule = models.CharField(max_length=100, blank=True)
    date = models.DateField(default=timezone.now)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.code_ue
    


from multiselectfield import MultiSelectField

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

    HEURES = [
            ('7h-9h55', '7h-9h55'),
            ('10h05-12h55', '10h05-12h55'),
            ('13h05-15h55', '13h05-15h55'),
            ('16h05-18h55', '16h05-18h55'),
            ('19h05-21h55', '19h05-21h55'),

            ('8h-10h', '8h-10h'),
            ('10h-12h', '10h-12h'),
            ('12h-14h', '12h-14h'),
            ('14h-16h', '14h-16h'),
            ('16h-18h', '16h-18h'),
            

    ]
    TYPES = [
        ('CM', 'CM'),
        ('TD', 'TD')
    ]

    jour = models.CharField(max_length=20, choices=JOURS)
    type = models.CharField(max_length=20, choices=TYPES)
    heure = models.CharField(max_length=12, choices=HEURES)
    date = models.DateField(default=timezone.now)
    
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    
    GROUPES = (
        ('G1','G1'), ('G2','G2'), ('G3','G3'), ('G4','G4'),
    )
    groupe = MultiSelectField(choices=GROUPES, blank=True)
        
    ue = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'self.salle lieux du cours'