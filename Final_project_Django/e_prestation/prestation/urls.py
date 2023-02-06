from django.urls import path
from prestation import views


urlpatterns = [ 
    path('',views.home,name='home'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('createPrestataires',views.createPrestataires,name='createPrestataires'),
    path('createAdresses',views.createAdresses,name='createAdresses'),
    path('createServices',views.createServices,name='createServices'),
    path('login',views.login_page, name='login'),
    path('logout', views.logout_user,name='logout'),
    path('register',views.signup_page, name='signup'),
    path('service/<int:service_id>/edit',views.edit_service, name='edit_service'),
    path('adresse/<int:adresse_id>/edit',views.edit_adresse, name='edit_adresse'),
    path('service/<int:user_id>',views.view_service, name='view_service'),
    path('mon_adresse/<int:user_id>',views.voir_adresse,name='mon_adresse'),
    path('mon_profile/<int:user_id>',views.profile,name='mon_profile'),
    path('profile/<int:user_id>',views.edit_prestataire,name="edit_profile"),
    path('categories/<int:categorie_id>',views.service_categories,name='categorie_service')



  ]