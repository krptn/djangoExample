from django.urls import path

from .views import SignUpView, LoginView, EnableMFA, LogoutView


urlpatterns = [
    path("signup/", SignUpView, name="signup"),
    path("login/", LoginView, name="login"),
    path("logout/", LogoutView, name="logout"),
    path("mfa/", EnableMFA, name="mfa")
]
