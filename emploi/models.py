from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Enseignant(models.Model):
	telephone = models.CharField(max_length=14)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="enseignant")
 
 
 
class UniteEneseignement(models.Model):
    
    nom_ue = models.CharField(max_length=40)
    
    

class  Filiere(models.Model):
    nom_filiere = models.CharField(max_length=30)
    
    
class Niveau(models.Model):
    nom_niveau = models.CharField(max_length=10)
    

class Groupe(models.Model):
    
    nom_groupe = models.CharField(max_length=20)
    

class Classes(models.Model):
    
    effectif_classe = models.IntegerField('Effectif')
    
    nom_classe = models.CharField(max_length=20)
    
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    


class Specialite(models.Model):
    
    nom_specialite = models.CharField(max_length=30)
    
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)


 
class Salle(models.Model):
    
    capacite_salle = models.IntegerField('capacite')
    
    
class Cours(models.Model):
    
    Salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    
    classe = models.ForeignKey(Classes, on_delete=models.CASCADE)
    
    ue = models.ForeignKey(UniteEneseignement, on_delete=models.CASCADE)
    


    