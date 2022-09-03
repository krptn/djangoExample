from django import forms
from krypton.auth.django import users

class UserCreationForm(forms.Form):
    Password = forms.CharField(widget=forms.PasswordInput)
    userName = forms.CharField(label = "User Name")
    age = forms.CharField(label = "Age")
    def save(self, commit=True):
        user = users.djangoUser(None)
        token = user.saveNewUser(pwd=self.cleaned_data["Password"], name=self.cleaned_data["userName"])
        user.setData("Age", self.cleaned_data["age"])
        return token, user.id

class LoginForm(forms.Form):
    userName = forms.CharField(label = "User Name")
    password = forms.CharField(widget=forms.PasswordInput)
    totp = forms.IntegerField(label = "TOTP")
    def save(self, commit=True):
        user = users.djangoUser(self.cleaned_data["userName"])
        token = user.login(pwd=self.cleaned_data["userName"], mfaToken=str(self.cleaned_data["totp"]))
        return token, user.id
