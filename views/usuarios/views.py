from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from app.models import Impressoras
from django.contrib.auth.models import User


def usuarios(request):
    iniciais_usuarios = []
    for usuario in User.objects.all():
        if usuario:
            iniciais_usuarios.append(str(usuario)[0])

    lista_iniciais_e_users = zip(iniciais_usuarios, User.objects.all())

    dados = {
        
        'lista_iniciais_e_users': lista_iniciais_e_users,
        'iniciais': str(request.user)[0],
        'impressoras': Impressoras.objects.all(),
        'usuario_logado': request.user
    }
    if request.user.is_authenticated:
        return render(request, 'app/usuarios.html', dados)
    else:
        return redirect('login')
