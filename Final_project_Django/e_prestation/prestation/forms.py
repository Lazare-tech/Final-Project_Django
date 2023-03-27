from django import forms
from .models import Prestataires,Adresses,Services,Categories
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models
# from .models import Commentaire
from django import forms
from .models import ReviewRating
#................................................................................................
#class forms

class PrestatairesForm(forms.ModelForm):
    edit_prestataire = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model=models.Prestataires
        fields=['nom','prenom','image','occupation','competences','niveauExperience']
class DeletePrestataireForm(forms.Form):
    delete_prestataire= forms.BooleanField(widget=forms.HiddenInput, initial=True)   
#................................................................................................
#class Adresses
class AdressesForm(forms.ModelForm):
    edit_adresse = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model=models.Adresses
        fields=('numeroTelephone','email','pays','ville') 
class DeleteAdressesForm(forms.Form):
    delete_adresse= forms.BooleanField(widget=forms.HiddenInput, initial=True)         
#................................................................................................
#class services
class ServicesForm(forms.ModelForm):
    edit_service = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    class Meta:
        model=models.Services
        fields=('name','titreConcert','tarif','image','description','categorie')
#class delete services
class DeleteServicesForm(forms.Form):
    delete_service= forms.BooleanField(widget=forms.HiddenInput, initial=True)
#................................................................................................
# class CommentaireForm(forms.ModelForm):
#     class Meta:
#         model=Commentaire
#         fields=['content']    
#


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
