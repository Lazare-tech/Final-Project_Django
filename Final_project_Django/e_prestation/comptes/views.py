from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . import forms
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
# Create your views here.
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages #import messages
from prestation.models import Prestataires
#.................................................................
#class logout

def logout_user(request):
    
    logout(request)
    return redirect('home')
#.........................................................................    
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
        message = 'Identifiants invalides.'
    return render(request, 'connexion/login.html', context={'form': form, 'message': message})
#.........................................................................    

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'connexion/register.html', context={'form': form})    
#..............................................
def profile(request,id):
    User = get_user_model()
    profile=User.objects.filter(id=id)
    context={
        'profile':profile
    }
    return render(request,'connexion/profile.html',context)
#........................................................
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users =get_user_model().objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "connexion/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
  
                    # messages.success(request,'A message with reset password instructions has been sent to your inbox.')

					return redirect ("/password_reset/done/")
			messages.error(request, 'An invalid email has been entered.')

	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="connexion/password/password_reset.html", context={"password_reset_form":password_reset_form})