from django import forms
from krypton.auth.django import users

class UserCreationForm(forms.Form):
    newPWD = forms.PasswordInput(label = "Password")
    userName = forms.CharField(label = "User Name")
    age = forms.CharField(label = "Age")
    def save(self, commit=True) -> users.djangoUser:
        user = users.djangoUser(None)
        user.saveNewUser(pwd=self.newPWD, name=self.userName)
        user.setData("Age", self.age)
        return user

class LoginForm(forms.Form):
    userName = forms.CharField(label = "User Name")
    password = forms.PasswordInput(label = "Password")
    totp = forms.IntegerField(label = "TOTP")
    def save(self, commit=True) -> users.djangoUser:
        user = users.djangoUser(self.userName)
        user.login(pwd=self.password, mfaToken=str(self.totp))
        return user

class PasswordResetForm(forms.Form):
    pass
