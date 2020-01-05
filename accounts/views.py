from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def register_view(request): 
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# save the user details. form.save() returns the user to us.
			user = form.save()
			#code to log user in goes here
			login(request, user)
			return HttpResponseRedirect("/online_order")
	else:
		# using django's inbuilt form
		form = UserCreationForm()
	context = {
		"form": form
	}
	return render(request, "accounts/register.html", context)

def login_view(request):
	# GET request when rendeing the login form. "POST" request when submitting the form.
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# code to log in the user goes here
			# no need to save as we're just validating and redirecting
			user = form.get_user()
			login(request, user)
			if "next" in request.POST:
				return HttpResponseRedirect(request.POST.get("next"))
			else:
				return HttpResponseRedirect("/online_order")
	else:
		form = AuthenticationForm()
	return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
	if request.method == "POST":
		# not neccessary to pass in 'user' as django knows we're logged in
		logout(request)
		return HttpResponseRedirect("login")

@login_required(login_url="login")
def user_view(request):
	return render(request, "accounts/user.html")

def index(request):
	if not request.user.is_authenticated:
		return render(request, "users/login.html", {"message": None})
	context = {
		"user": request.user
	}
	return render(request, "users/user.html", context)

# below code would be if not using django's forms

# def login_view(request):
# 	username = request.POST["username"]
# 	password = request.POST["password"]
# 	user = authenticate(request, username=username, password=password)
# 	if user is not None:
# 		#login is a django function
# 		login(request, user)
# 		#using "HttpResponseRedirect" rather than "render" takes us through the index function 
# 		#before rendering index.html and this is in case computation is required before rendering. 
# 		#reverse allows us to go from "index" ie the name of the route "" in urls.py without worrying
# 		#about the url name and so would be valid even if url name were changed.
# 		return HttpResponseRedirect(reverse("index"))
# 	else:
# 		return render(request, "users/login.html", {"message": "invalid credentials"})

# def logout_view(request):
# 	#logout is a django function in django.contrib.auth
# 	logout(request)
# 	return render(request, "users/login.html", {"message": "logged out"})

