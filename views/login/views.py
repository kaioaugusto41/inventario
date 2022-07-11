from django.contrib import messages
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario', False)
        senha = request.POST.get('senha', False)
        print(usuario, senha)
        return redirect('index')
    else:
        return render(request, 'login/login.html')
    