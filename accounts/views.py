from django.shortcuts import render

# Create your views here.
# accounts/views.py
from . import forms
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.http.request import HttpRequest

def SignUpView(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'registration/signup.html', {'form': forms.UserCreationForm})
    form = forms.UserCreationForm(request.POST)
    token, Uid = form.save()
    response = redirect("mfa")
    response.set_cookie("_KryptonUserID", Uid)
    response.set_cookie("_KryptonSessionToke", token, 15*60)
    return response

def LoginView(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'registration/login.html', {'form': forms.LoginForm})
    form = forms.LoginForm(request.POST)
    token, Uid = form.save()
    response = redirect("/")
    response.set_cookie("_KryptonUserID", Uid)
    response.set_cookie("_KryptonSessionToke", token, 15*60)
    return response

@login_required
def RecoveryCodeView(request: HttpRequest):
    return render(request, "register/resetEnable.html", {'codes': request.user.enablePWDReset()})

@login_required
def EnableMFA(request: HttpRequest):
    secret, qr = request.user.enableMFA()
    return render(request, "register/mfa.html", {"codes": secret, "qr": qr})
