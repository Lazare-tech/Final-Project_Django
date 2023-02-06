from django.shortcuts import render
from prestation.models import Prestataires, Services,Categories,Adresses
from .forms import PrestatairesForm,AdressesForm,ServicesForm,DeleteServicesForm,DeleteAdressesForm,DeletePrestataireForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import AbstractUser,User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . import forms
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.conf import settings
from . import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.
#home page
def home(request):
    categories=Categories.objects.all()
    services=Services.objects.all()
   
    return render(request,'base.html',{'categories':categories,'services':services})
#------------------------------------------------------------------------------------
def profile(request,user_id):
    profile=Prestataires.objects.filter(author_id=user_id)
    context={
            'profile':profile
        }
    return render(request,'forms/mon_profile.html',context)
#------------------------------------------------------------------------------------

#class detail service
@login_required
def detail(request,id):
    adresses=Adresses.objects.filter(id=id)
    prestataires=Prestataires.objects.filter(id=id)
    categories=Categories.objects.all()

    return render(request,'detail.html',{'adresses':adresses,'prestataires':prestataires,
                                        'categories':categories})
#------------------------------------------------------------------------------------
#class creation de prestataires
@login_required
def createPrestataires(request):
    categories=Categories.objects.all()
    form= forms.PrestatairesForm()
    if request.method == 'POST':
        form=forms.PrestatairesForm(request.POST or None, request.FILES)
        if form.is_valid(): 
            form= form.save(commit=False)
            form.author= request.user
            form.save()
            form=PrestatairesForm()
            return redirect('view_service',request.user.id)
    return render(request,'forms/createPrestataires.html',{'form':form,'categories':categories})
#------------------------------------------------------------------------------------


def edit_prestataire(request, user_id):
    prestataire = get_object_or_404(models.Prestataires, id=user_id)
    # s=Services.objects.filter(models.Services,author_id=service_id)
    edit_form = forms.PrestatairesForm(instance=prestataire)
    delete_form = forms.DeletePrestataireForm()
    if request.method == 'POST':
        if 'edit_prestataire' in request.POST:
            edit_form = forms.PrestatairesForm(request.POST, instance=prestataire)
            if edit_form.is_valid():
                edit_form.save()
                messages.success(request,'Profile modifier avec success')
                return redirect('mon_profile',request.user.id)
        if 'delete_prestataire' in request.POST:
            delete_form = forms.DeletePrestataireForm(request.POST)
            if delete_form.is_valid():
                prestataire.delete()
                messages.success(request,'Service suprimer avec success')
                return redirect('view_service',request.user.id)    
    
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }
    return render(request,'profile_user/edit_prestataire.html',context)
#------------------------------------------------------------------------------------
#formulaire adresses
@login_required
def createAdresses(request):
    categories=Categories.objects.all()
    # print(adresse.prestataire.nom)
    form=forms.AdressesForm()
    if request.method == 'POST':
        form=forms.AdressesForm(request.POST or None)
        if form.is_valid():
            form=form.save(commit=False)
            form.author =request.user
            form.save()
            form=AdressesForm()
            return redirect('home')
    return render(request,'forms/createAdresses.html',{'form':form,'categories':categories})

def voir_adresse(request,user_id):
    adresse=Adresses.objects.filter(author_id=user_id)
    context={
        'adresse':adresse
    }
    return render(request,'profile_user/voir_adresse.html',context)
def service_categories(request,categorie_id):
    services=Services.objects.filter(categorie_id=categorie_id)
    categories=Categories.objects.all()
    context={
        'services':services,
        'categories':categories,
    }
    return render(request,'services/service.html',context)
#-------------------------------------------------------------------

@login_required
def edit_adresse(request, adresse_id):

    adresse = get_object_or_404(models.Adresses, id=adresse_id)
    edit_form = forms.AdressesForm(instance=adresse)
    delete_form = forms.DeleteAdressesForm()
    if request.method == 'POST' :
            if 'edit_adresse' in request.POST:
                edit_form = forms.AdressesForm(request.POST, instance=adresse)
                if edit_form.is_valid():
                    edit_form.save()
                    messages.success(request,'Adresse modifier avec success')
                    return redirect('mon_adresse',request.user.id)
            
            if 'delete_adresse' in request.POST:    
                delete_form = forms.DeleteAdressesForm(request.POST)
                if delete_form.is_valid():
                        adresse.delete()
                        return redirect('home')    
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        'adresse':adresse,
        }
    return render(request, 'profile_user/edit_adresse.html', context=context)
#...............................................................
# def mon_adresse(request):
#         mon_adresse=Adresses.objects.filter(id=request.user)
#         return render(request, 'profile_user/edit_adresse.html', {'mon_adresse':mon_adresse})


#------------------------------------------------------------------------------------
#form services
@login_required
def createServices(request):
    categories=Categories.objects.all()
    form= forms.ServicesForm()
    if request.method == 'POST':
        form=forms.ServicesForm(request.POST or None, request.FILES)

        if form.is_valid():
            form=form.save(commit=False)

            form.author = request.user
            form.save()
            form=ServicesForm()
            return redirect('mon_adresse',request.user.id)
            # return redirect('mon_adresse',request.user.id)
    return render(request,'forms/createServices.html',{'form':form,'categories':categories})
#edit services
@login_required
def edit_service(request, service_id):
    service = get_object_or_404(models.Services, id=service_id)
    # s=Services.objects.filter(models.Services,author_id=service_id)
    edit_form = forms.ServicesForm(instance=service)
    delete_form = forms.DeleteServicesForm()
    if request.method == 'POST':
        if 'edit_service' in request.POST:
            edit_form = forms.ServicesForm(request.POST, instance=service)
            if edit_form.is_valid():
                edit_form.save()
                messages.success(request,'Service modifier avec success')
                return redirect('view_service',request.user.id)
        if 'delete_service' in request.POST:
            delete_form = forms.DeleteServicesForm(request.POST)
            if delete_form.is_valid():
                service.delete()
                messages.success(request,'Service suprimer avec success')
                return redirect('view_service',request.user.id)    
    
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }
    return render(request, 'profile_user/edit_service.html', context=context)

@login_required
def view_service(request, user_id):
    # service = get_object_or_404(models.Services, id=service_id)
    service=Services.objects.filter(author_id=user_id)
    return render(request, 'profile_user/view_service.html', {'service': service})
#............................................................................................
#deconnection methode
def logout_user(request):
    
    logout(request)
    return redirect('home')
#..........................................................................................
#connection methode
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'connection/login.html', context={'form': form})
#...............................................................................................
#register methode
def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            # login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'connection/register.html', context={'form': form})    
#.....................................................................................
