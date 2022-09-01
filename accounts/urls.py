from django.urls import path

from .views import SignUpView, LoginView, RecoveryCodeView, EnableMFA


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("reset/", RecoveryCodeView, name="reset"),
    path("login/", LoginView, name="login"),
    path("mfa/", EnableMFA, name="MFA")
]