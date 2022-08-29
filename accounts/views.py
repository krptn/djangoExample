from django.shortcuts import render

# Create your views here.
# accounts/views.py
import forms
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render


class SignUpView(generic.CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class PasswordReset(generic.CreateView):
    form_class = forms.PasswordResetForm
    success_url = reverse_lazy("login")
    template_name = "registration/reset.html"

class Login(generic.CreateView):
    form_class = forms.LoginForm
    success_url = reverse_lazy("/")
    template_name = "registration/login.html"
