from django.contrib import admin
from .models import Prestataires,Adresses,Categories,Services,ReviewRating,ServicesGallery
import admin_thumbnails
#
@admin_thumbnails.thumbnail('image')
class ServicesGalleryInline(admin.TabularInline):
    model = ServicesGallery
    extra = 1
# Register your models here.
class AdminPrestataires(admin.ModelAdmin):
    list_display=('id','nom','prenom','image','occupation','competences','niveauExperience')
admin.site.register(Prestataires,AdminPrestataires)
#..................................................................................................
#adresses
class AdressesAdmin(admin.ModelAdmin):
    list_display=('id','numeroTelephone','email','pays','ville')
admin.site.register(Adresses,AdressesAdmin)

#..................................................................................................
#services
class ServicesAdmin(admin.ModelAdmin):
    list_display=('id','name','titreConcert','tarif','image','categorie','description')
    inlines = [ServicesGalleryInline]
admin.site.register(Services,ServicesAdmin)

#Avis
# class AdminAvis(admin.ModelAdmin):
#     list_display=('id','content','author')
# admin.site.register(Commentaire,AdminAvis)

#..................................................................................................
#categories
# class AdminCategories(admin.ModelAdmin):
#     list_display=('nom')
admin.site.register(Categories)

#..................................................................................................

class ReviewRatingAdmin(admin.ModelAdmin):
    list_display=['service','user','subject','review','rating','ip','status','created_at','updated_at']
admin.site.register(ReviewRating,ReviewRatingAdmin)
#........................................................
class ServiceGalleryAdmin(admin.ModelAdmin):
    list_display=['service','image']
admin.site.register(ServicesGallery,ServiceGalleryAdmin)
