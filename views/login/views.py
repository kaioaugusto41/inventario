from django.contrib import messages, auth
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario', False)
        senha = request.POST.get('senha', False)
        if usuario == '' or senha == '':
            messages.error(request, 'Os campos Usuário e Senha não podem ficar vazios!')
            return redirect('login')
        if not User.objects.filter(username=usuario).exists():
            messages.error(request, 'O usuário {} não existe :('.format(usuario))
            return redirect('login')
        else:
            nome = User.objects.filter(username=usuario).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=usuario, password=senha)
            print(nome)
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou Senha incorretos :(')
                return redirect('login')

    else:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'login/login.html')
    