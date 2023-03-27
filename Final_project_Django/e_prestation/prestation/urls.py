from django.urls import path
from prestation import views


urlpatterns = [ 
    path('',views.home,name='home'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('createPrestataires',views.createPrestataires,name='createPrestataires'),
    #services
    path('createServices',views.createServices,name='createServices'),
    path('service/<int:service_id>/edit',views.edit_service, name='edit_service'),
    path('service/<int:user_id>',views.view_service, name='view_service'),
    #adresse
    path('createAdresses',views.createAdresses,name='createAdresses'),    
    path('adresse/<int:adresse_id>/edit',views.edit_adresse, name='edit_adresse'),
     path('mon_adresse/<int:user_id>',views.voir_adresse,name='mon_adresse'),
    #profile
    path('mon_profile/<int:user_id>',views.profile,name='mon_profile'),
    path('profile/<int:user_id>',views.edit_prestataire,name="edit_profile"),
    path('categories/<int:categorie_id>',views.service_categories,name='categorie_service'),
    #comment
    path('comment/<int:pk>/add', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/', views.comment_detail, name='comment_detail'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # path('post/<int:id>',views.post,name="post_detail"),
    #
    path('rate/<int:service_id>/<int:rating>/', views.rate),
    #
    path('submit_review/<int:services_id>/', views.submit_review, name='submit_review'),


  ]