from django.http.request import HttpRequest
from django.shortcuts import render

def homeView(request: HttpRequest):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'name': request.user.userName, 'age': request.user.getData('Age').decode(), 'authenticated': True})
    else:
        return render(request, 'home.html', {'name': "None", 'age': "None", 'authenticated': False})