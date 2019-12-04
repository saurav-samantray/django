from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import logout

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
	context = {
		"title":"Hello World",
		"content" : "Welcome to Homepage",
		}
	if request.user.is_authenticated():
		context['premium_content'] = '$10 off'
		context['username'] = request.user
	return render(request, "homepage.html", context)

def about_page(request):
	context = {
		"title":"About Page",
		"content" : "Welcome to About page"
		}
	return render(request, "homepage.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"Contact Page",
		"content" : "Welcome to Contact page",
		"form" : contact_form,
		}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	return render(request, "contact/view.html", context)

def login_page(request):
	login_form = LoginForm(request.POST or None)
	context = {
		"title":"Login Page",
		"content" : "Welcome to Login page",
		"form" : login_form
		}
	#print(request.user.is_authenticated())
	if login_form.is_valid():
		print(login_form.cleaned_data)
		context['form'] = LoginForm()
		username = login_form.cleaned_data.get('username')
		password = login_form.cleaned_data.get('password')
		user = authenticate(request,username=username,password=password)
		print(user)
		#print(request.user.is_authenticated())
		if user is not None:
			login(request,user)
			#print(request.user.is_authenticated())
			#redirect to success page
			#context['form'] = LoginForm()
			return redirect("home")
		else:
			#return an invalid login error message
			print("Login error")
	return render(request, "auth/login.html", context)

def logout_request(request):
    logout(request)
    #messages.info(request, "Logged out successfully!")
    return redirect("home")


User = get_user_model()
def register_page(request):
	register_form = RegisterForm(request.POST or None)
	context = {
		"form" : register_form
		}
	if register_form.is_valid():
		print(register_form.cleaned_data)
		username = register_form.cleaned_data.get('username')
		email = register_form.cleaned_data.get('email')
		password = register_form.cleaned_data.get('password')
		new_user = User.objects.create_user(username,email,password)
		print(new_user)
	else:
		print("Error in form")
	return render(request, "auth/register.html", context)
