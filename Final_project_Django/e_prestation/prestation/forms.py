from django import forms
from .models import Prestataires,Adresses,Services,Categories
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

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
#class login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    
#................................................................................................
#register form
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # model= User
        fields = ('username', 'email','password1', 'password2')
#class userform
# class UserForm(UserCreationForm):
#     class Meta:
#         model= User
#         fields=('username','password1','password2')
