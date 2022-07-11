from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages

def sair(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso :)')
    return redirect('login')
