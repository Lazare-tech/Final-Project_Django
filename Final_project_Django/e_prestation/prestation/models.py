from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings

# Create your models here.
#class categories
class Categories(models.Model):
    nom=models.CharField(max_length=30,blank=True)  
    #class meta
    class Meta:
        verbose_name=("Categories")
        verbose_name_plural=("Categories")
    def __str__(self):
        return self.nom  
#...........................................................................
 
class Prestataires(models.Model):
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    image=models.ImageField(upload_to='Images',blank=True)
    occupation=models.CharField(max_length=30)
    competences=models.CharField(max_length=30)
    niveauExperience=models.CharField(max_length=30)
    author =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    
    #classe meta
    class Meta:
        
        verbose_name=("Prestataires")
        verbose_name_plural=("Prestataires")
    def __str__(self):
        return self.nom
#...........................................................................   
#class adresse prestataire
class Adresses(models.Model):
    numeroTelephone=models.CharField(max_length=30)
    email=models.EmailField()
    pays=models.CharField(max_length=30)
    ville=models.CharField(max_length=30)
    # prestataire=models.OneToOneField(Prestataires,on_delete=models.CASCADE,blank=True)
    author =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name=("Adresses")
        verbose_name_plural=("Adresses")
    def __str__(self):
        return self.numeroTelephone
#...........................................................................
#service prestataire
        
class Services(models.Model):
    name=models.CharField(max_length=30)
    titreConcert=models.CharField(max_length=30, blank=True)
    tarif=models.DecimalField(max_digits=10,decimal_places=6)
    image=models.ImageField(upload_to='Images',blank=True)
    description=models.TextField()
    categorie=models.ForeignKey(Categories,on_delete=models.CASCADE)
    author =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # prestataires=models.ForeignKey(Prestataires,on_delete=models.CASCADE,blank=True)
    #les meta data travaillent sur les donnees de la grande classe
    class Meta:
        verbose_name=("Services")
        verbose_name_plural=("Services")
    #surcharge methode pour afficher les produits dans la base de donnee    
    def __str__(self):
        return self.name
#...........................................................................
class Avis(models.Model):
    text=models.TextField()
    avis=models.ForeignKey(Services,on_delete=models.CASCADE)
    author =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
            return self.text
        
    
class User(AbstractUser):
    pass
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
    (CREATOR, 'Créateur'),
    (SUBSCRIBER, 'Abonné'),
    )   
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    # user=models.ForeignKey(Services, on_delete=models.CASCADE)
