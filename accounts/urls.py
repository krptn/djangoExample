from django.urls import path

from .views import SignUpView, PasswordReset, Login


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("reset/", PasswordReset.as_view(), name="reset"),
    path("login/", Login.as_view(), name="login")
]