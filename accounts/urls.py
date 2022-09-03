from django.urls import path

from .views import SignUpView, LoginView, RecoveryCodeView, EnableMFA, LogoutView


urlpatterns = [
    path("signup/", SignUpView, name="signup"),
    path("reset/", RecoveryCodeView, name="reset"),
    path("login/", LoginView, name="login"),
    path("logout/", LogoutView, name="logout"),
    path("mfa/", EnableMFA, name="mfa")
]
