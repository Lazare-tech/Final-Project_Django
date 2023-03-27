from django.shortcuts import render,HttpResponse
from prestation.models import Prestataires, Services,Categories,Adresses,Rating,ServicesGallery
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
from .models import  ReviewRating
from .forms import ReviewForm

# Create your views here.
#home page
def home(request):
    categories=Categories.objects.all()
    services=Services.objects.all()
    
    # for service in services:
    #     ratings = Rating.objects.filter(service_id=service).first()
    #     rating=ratings.objects.filter(user=request.user)
    #     service.user_rating = rating.rating if rating else 0
    return render(request,'base.html',{'categories':categories,'services':services})
#
def rate(request, service_id: int, rating: int) -> HttpResponse:
    post = Services.objects.get(id=service_id)
    Rating.objects.filter(post=post, user=request.user).delete()
    post.rating_set.create(user=request.user, rating=rating)
    return render(request,'base.html')
#.....................................................................................
#categories

def service_categories(request,categorie_id):
    services=Services.objects.filter(categorie_id=categorie_id)
    categories=Categories.objects.all()
    context={
        'services':services,
        'categories':categories,
    }
    return render(request,'services/service.html',context)
#------------------------------------------------------------------------------------
def profile(request,user_id):
    profile=Prestataires.objects.filter(author_id=user_id)
    context={
            'profile':profile
        }
    return render(request,'profile/mon_profile.html',context)

#------------------------------------------------------------------------------------
#PRESTATAIRES
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
    return render(request,'prestataires/createPrestataires.html',{'form':form,'categories':categories})

#-----------
#modifier un prestataire
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
    return render(request,'prestataires/edit_prestataire.html',context)
#------------------------------------------------------------------------------------
                        #ADRESSE
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
    return render(request,'adresse/createAdresses.html',{'form':form,'categories':categories})
#-----------
def voir_adresse(request,user_id):
    adresse=Adresses.objects.filter(author_id=user_id)
    context={
        'adresse':adresse
    }
    return render(request,'adresse/voir_adresse.html',context)

#----------

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
    return render(request, 'adresse/edit_adresse.html', context=context)
#...............................................................
# def mon_adresse(request):
#         mon_adresse=Adresses.objects.filter(id=request.user)
#         return render(request, 'profile_user/edit_adresse.html', {'mon_adresse':mon_adresse})


#------------------------------------------------------------------------------------
                                #SERVICES
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
    return render(request,'services/createServices.html',{'form':form,'categories':categories})

#--------edit services
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
    return render(request, 'services/edit_service.html', context=context)

#-----------
@login_required
def view_service(request, user_id):
    # service = get_object_or_404(models.Services, id=service_id)
    service=Services.objects.filter(author_id=user_id)
    
    return render(request, 'services/view_service.html', {'service': service})
#..........
#class detail service
@login_required
def detail(request,id):
    
    service=Services.objects.get(pk=id)
    
    prestataires=Prestataires.objects.filter(author=service.author)
    services=Services.objects.get(id=id)
    adresses=Adresses.objects.filter(author=service.author)
    # single_product = Services.objects.get(category__slug=category_slug, slug=product_slug)
    reviews = ReviewRating.objects.filter(service_id=services.id, status=True)
    service_gallery = ServicesGallery.objects.filter(service_id=services.id)
    print(service_gallery)

    # print(services)
    # services=Services.objects.all()


    categories=Categories.objects.all()
    # comment=Commentaire.objects.filter(comment_id=id)
    

    return render(request,'detail.html',{'adresses':adresses,'prestataires':prestataires,
                                        'categories':categories,'services':services,'reviews':reviews,'service_gallery':service_gallery})
#..............................................................................
@login_required
def add_comment(request,pk):
    service_commentaire=get_object_or_404(Services,pk=pk)
    # form_c= forms.CommentaireForm()
    if request.method== 'POST':
        form=CommentaireForm(request.POST)

        # form=forms.CommentaireForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.comment=service_commentaire
            comment.author=request.user 
            comment.save()
            return redirect('comment_detail',pk=comment.pk)
    else:
        form=CommentaireForm()
    return render(request,'comment/add_comment.html',{'form':form})
#
@login_required
def comment_detail(request,pk):
    comment=get_object_or_404(Commentaire,pk=pk)
    return render(request,'comment/comment_detail.html',{'comment':comment})
#
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Commentaire, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.comment.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Commentaire, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.comment.pk)
# #
# def post(request,id):
#     comment=Commentaire.objects.filter(pk=id)
#     return render(request,'post_detail',{'comment':comment})
#
def submit_review(request, services_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, service__id=services_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.service_id = services_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)
#

# def product_detail(request, category_slug, product_slug):
#     try:
#         single_product = Services.objects.get(category__slug=category_slug, slug=product_slug)
#         in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
#     except Exception as e:
#         raise e

#     if request.user.is_authenticated:
#         try:
#             orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
#         except OrderProduct.DoesNotExist:
#             orderproduct = None
#     else:
#         orderproduct = None

#     # Get the reviews
#     reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

#     # Get the product gallery
#     product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

#     context = {
#         'single_product': single_product,
#         'in_cart'       : in_cart,
#         'orderproduct': orderproduct,
#         'reviews': reviews,
#         'product_gallery': product_gallery,
#     }
#     return render(request, 'store/product_detail.html', context)
