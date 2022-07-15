from datetime import datetime
from django.contrib import messages
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from app.models import Logs
from views.index.views import usuarios

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', False)
        sobrenome = request.POST.get('sobrenome', False)
        email = request.POST.get('email', False)
        usuario = request.POST.get('usuario', False)
        senha = request.POST.get('senha', False)
        senha_confirmacao = request.POST.get('senha_confirmacao', False)
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Não foi possível cadastrar o usuário pois já existe um com este endereço e-mail :(')
            return redirect('index')
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Não foi possível cadastrar o usuário pois já existe um com este usuário :(')
            return redirect('index')
        if senha != senha_confirmacao:
            messages.error(request, 'As senhas não são iguais :(')
            return redirect('index')
        if len(senha) < 6:
            messages.error(request, 'A senha não pode ser menor que 6 caracteres :(')
            return redirect('index')
        if usuario.count('.') < 1 or usuario.count('.') > 1:
            messages.error(request, 'O nome de usuário {} não é válido, tente neste formato: exemplo.usuario'.format(usuario))
            return redirect('index')
        if usuario[:usuario.index('.')].lstrip() == '' or usuario[usuario.index('.')+1:].lstrip() == '':
            messages.error(request, 'O nome de usuário {} não é válido, tente neste formato: exemplo.usuario'.format(usuario))
            return redirect('index')
        else:
            User.objects.create_user(first_name=nome, last_name=sobrenome, email=email, username=usuario, password=senha).save()
            messages.success(request, 'Usuário {} cadastrado com sucesso :)'.format(usuario))
            Logs.objects.create(acao='Cadastro de usuário', data=datetime.now(), descricao=
                'Foi realizado o cadastro do(a) usuário(a) {}'.format(usuario), 
                usuario=str(request.user)
                ).save(),

    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')

def deleta_usuario(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            usuario = request.POST.get('usuario', False)
            User.objects.filter(username=usuario).delete()
            messages.success(request, 'Usuário {} excluído com sucesso!'.format(usuario))
            Logs.objects.create(acao='Exclusão de usuário', data=datetime.now(), descricao=
                'Foi realizada a exclusão do usuário {}'.format(usuario), 
                usuario=str(request.user)
                ).save()
            return redirect('usuarios')
        return redirect('usuarios')
    else:
        return redirect('login')

def suspende_usuario(request):
    if request.user.is_authenticated:
        usuario = request.POST.get('usuario', False)
        User.objects.filter(username=usuario).update(is_active=False)
        messages.success(request, 'O usuário {} foi suspenso com sucesso :)'.format(usuario))
        Logs.objects.create(acao='Suspensão de usuário', data=datetime.now(), descricao=
                'Foi realizada a suspensão do usuário {}'.format(usuario), 
                usuario=str(request.user)
                ).save()
        return redirect('usuarios')
    else:
        return redirect('login')

def ativa_usuario(request):
    if request.user.is_authenticated:
        usuario = request.POST.get('usuario', False)
        User.objects.filter(username=usuario).update(is_active=True)
        messages.success(request, 'O usuário {} foi ativo com sucesso :)'.format(usuario))
        Logs.objects.create(acao='Ativação de usuário', data=datetime.now(), descricao=
                'Foi realizada a ativação do usuário {}'.format(usuario), 
                usuario=str(request.user)
                ).save()
        return redirect('usuarios')
    else:
        return redirect('login')


