from django.shortcuts import render
from Dash.register import userForm

def login(request):
    data = {}
    data['register'] = userForm()
    return render(request, 'login.html', data)

def register(request):
    data = {}
    data['register'] = userForm()
    return render(request, 'register.html', data)