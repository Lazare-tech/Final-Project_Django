from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Prestataires,Adresses,Categories,Services,User,Avis
# Register your models here.
class AdminPrestataires(admin.ModelAdmin):
    list_display=('id','nom','prenom','image','occupation','competences','niveauExperience')
admin.site.register(Prestataires,AdminPrestataires)
#..................................................................................................
#adresses
class AdminAdresses(admin.ModelAdmin):
    list_display=('id','numeroTelephone','email','pays','ville')
admin.site.register(Adresses,AdminAdresses)

#..................................................................................................
#services
class AdminServices(admin.ModelAdmin):
    list_display=('id','name','titreConcert','tarif','image','categorie','description')
admin.site.register(Services,AdminServices)

#Avis
class AdminAvis(admin.ModelAdmin):
    list_display=('id','text','author')
admin.site.register(Avis,AdminAvis)

#..................................................................................................
#categories
# class AdminCategories(admin.ModelAdmin):
#     list_display=('nom')
admin.site.register(Categories)

#..................................................................................................
class AdminUser(admin.ModelAdmin):
    list_display=('id','username','first_name','last_name','email','password','is_staff','is_active','date_joined')
admin.site.register(User,AdminUser)

