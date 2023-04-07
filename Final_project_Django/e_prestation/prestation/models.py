from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
from django.db.models import Avg
from comptes.models import User
from django.db.models import Avg, Count
from django.urls import reverse

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
    en_ligne = models.BooleanField(default=False)
    
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
    header = models.CharField(max_length=100, default="Header")

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
    
    # def get_url(self):
    #     return reverse('service_detail', args=[self.category.slug, self.slug])
    def averageReview(self):
        reviews = ReviewRating.objects.filter(service=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(service=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
#...........................................................................
class ReviewRating(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
#---------------------------------------------
    
# class Commentaire(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
#     created_on = models.DateTimeField(auto_now=True)
#     last_updated = models.DateField(blank=True, null=True)
#     published = models.BooleanField(default=False, verbose_name="Publié")
#     content = models.TextField(blank=True, verbose_name="Contenu")
#     comment=models.ForeignKey(Services,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.content
#.....................................................
class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.service.header}: {self.rating}"
    
class ServicesGallery(models.Model):
    service = models.ForeignKey(Services, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/services', max_length=255)

    def __str__(self):
        return self.service.name

    class Meta:
        verbose_name = 'servicegallery'
        verbose_name_plural = 'service gallery'
