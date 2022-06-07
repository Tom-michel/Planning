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
    

class Groupe(models.Model):
    nom_groupe = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nom_groupe
    

class Classe(models.Model):
    effectif_classe = models.IntegerField('Effectif')
    date = models.DateField(default=timezone.now)  
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.filiere}-{self.niveau}'
    


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
    intitule = models.CharField(max_length=100, unique=True)
    date = models.DateField(default=timezone.now)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.intitule
    


from multiselectfield import MultiSelectField

class Cours(models.Model):
    JOURS = [
        ('lundi', 'lundi'),
        ('mardi', 'mardi'),
        ('mercredi', 'mercredi'),
        ('jeudi', 'jeudi'),
        ('vendredi', 'vendredi'),
        ('samedi', 'samedi'),
        ('dimanche', 'dimanche')
    ]
    TYPES = [
        ('CM', 'CM'),
        ('TD', 'TD')
    ]

    jour = models.CharField(max_length=20, choices=JOURS)
    type = models.CharField(max_length=20, choices=TYPES)
    heure = models.CharField(max_length=12)
    date = models.DateField(default=timezone.now)
    
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    
    GROUPES = (
        ('G1','G1'), ('G2','G2'), ('G3','G3'), ('G4','G4'),
    )
    groupe = MultiSelectField(choices=GROUPES)
        
    ue = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'self.salle lieux du cours'
    
