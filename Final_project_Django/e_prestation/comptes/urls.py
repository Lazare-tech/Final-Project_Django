from django.urls import path
from comptes import views 
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('login',views.login_page, name='login'),
    path('logout', views.logout_user,name='logout'),
    path('register',views.signup_page, name='signup'),    
    path('profile/<int:id>',views.profile,name='profile'),
    path("password_reset", views.password_reset_request, name="password_reset"),

    #
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='connexion/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="connexion/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='connexion/password/password_reset_complete.html'), name='password_reset_complete'),      


  ]