from django.shortcuts import render

# Create your views here.
# accounts/views.py
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest

def SignUpView(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'registration/signup.html', {'form': forms.UserCreationForm})
    form = forms.UserCreationForm(request.POST)
    if form.is_valid():
        token, Uid = form.save()
        response = redirect("mfa")
        response.set_cookie("_KryptonUserID", Uid)
        response.set_cookie("_KryptonSessionToken", token, 15*60)
        return response

def LoginView(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'registration/login.html', {'form': forms.LoginForm})
    form = forms.LoginForm(request.POST)
    if form.is_valid():
        token, Uid = form.save()
        response = redirect("/")
        response.set_cookie("_KryptonUserID", Uid)
        response.set_cookie("_KryptonSessionToken", token, 15*60)
        return response

@login_required
def EnableMFA(request: HttpRequest):
    secret, qr = request.user.enableMFA()
    return render(request, "registration/mfa.html", {"secret": secret.decode(), "qr": qr})

@login_required
def LogoutView(request: HttpRequest):
    request.user.logout()
    response = redirect("/")
    response.set_cookie("_KryptonUserID", '', 0)
    response.set_cookie("_KryptonSessionToken", '', 0)
    return response
