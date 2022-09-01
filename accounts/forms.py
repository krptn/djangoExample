from django import forms
from krypton.auth.django import users

class UserCreationForm(forms.Form):
    Password = forms.CharField(widget=forms.PasswordInput)
    userName = forms.CharField(label = "User Name")
    age = forms.CharField(label = "Age")
    def save(self, commit=True):
        user = users.djangoUser(None)
        token = user.saveNewUser(pwd=self.Password, name=self.userName)
        user.setData("Age", self.age)
        return token, user.id

class LoginForm(forms.Form):
    userName = forms.CharField(label = "User Name")
    password = forms.CharField(widget=forms.PasswordInput)
    totp = forms.IntegerField(label = "TOTP")
    def save(self, commit=True):
        user = users.djangoUser(self.userName)
        token = user.login(pwd=self.password, mfaToken=str(self.totp))
        return token, user.id

class PasswordResetForm(forms.Form):
    userName = forms.CharField(label = "User Name")
    otp = forms.IntegerField(label = "OTP")
    NewPassword = forms.CharField(widget=forms.PasswordInput)
    def save(self, commit=True):
        user = users.djangoUser(self.userName)
        token = user.resetPWD(str(self.otp), self.NewPassword)
        return token
