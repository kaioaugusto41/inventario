from datetime import datetime
from django.contrib import messages
import imp
from django.shortcuts import render, redirect
from app.models import Impressoras, Logs, solicitacoes
from views.index.funcoes.adiciona_impressora import adiciona_impressora
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        print(solicitacoes.objects.all())

        dados = {
            'solicitacoes_em_aberto': solicitacoes.objects.filter(status_aberto=True),
            'iniciais': str(str(request.user))[0],
            'impressoras': Impressoras.objects.all()
        }
        
        return render(request, 'app/index.html', dados)
    else:
        return redirect('login')

def impressoras(request):

    lista_codigos = []
    lista_ips = []
    for impressora in Impressoras.objects.all():
        lista_codigos.append(str(impressora.codigo))
        lista_ips.append(str(impressora.ip))

    # EDITA AS IMPRESSORAS
    if request.method == 'GET':
        funcao = request.GET.get('funcao')
        
        if funcao == 'edita_impressora':
            codigo = request.GET.get('codigo', False)
            setor = request.GET.get('setor', False)
            marca = request.GET.get('marca', False)
            modelo = request.GET.get('modelo', False)
            toners_estoque = request.GET.get('toners_estoque', False)
            ip = request.GET.get('ip', False)
            impressora_a_editar = Impressoras.objects.filter(codigo=codigo)
            impressora_a_editar.update(codigo=codigo, setor=setor, marca=marca, modelo=modelo, qtd_toners=toners_estoque, ip=ip)
            if codigo != False:
                messages.success(request, 'Impressora editada com sucesso! :)')
                Logs.objects.create(acao='Edição de impressora', data=datetime.now(), descricao=
                'Foi realizada alterações na impressora cujo código de indentificação é {}'.format(codigo), 
                usuario=str(request.user)
                ).save(),
                return redirect('index')



    if request.method == 'POST':
        funcao = request.POST.get('funcao')

        if funcao == 'adiciona_impressora':
            codigo = request.POST.get('codigo', False).upper()
            setor = request.POST.get('setor', False).title()
            marca = request.POST.get('marca', False).title()
            modelo = request.POST.get('modelo', False).upper()
            toners_estoque = request.POST.get('toners_estoque', False)
            ip = request.POST.get('ip', False)
                
            # Valida existência do código
            if codigo in lista_codigos:
                messages.error(request, 'Não foi possível adicionar a impressora pois já existe uma com este código :(')
                return redirect('index')

            # Valida existência do ip
            if ip in lista_ips:
                messages.error(request, 'Não foi possível adicionar a impressora pois já existe uma com este endereço IP :(')
                return redirect('index')

            # Valida tamanho do ip
            if len(ip) < 10 or ip.count('.') != 3:
                messages.error(request, 'O endereço IP {} não é um IP válido :('.format(ip))
                return redirect('index')
            
            # ADICIONA A IMPRESSORA
            else:
                adiciona_impressora(request, codigo, setor, marca, modelo, toners_estoque, ip)
                Logs.objects.create(acao='Cadastro de impressora', data=datetime.now(), descricao=
                'Foi realizado o cadastro de uma nova impressora, cujo código de identificação é {}'.format(codigo), 
                usuario=str(request.user)
                ).save(),
                return redirect('index')


        if funcao == 'exclui_impressora':
            codigo = request.POST.get('codigo', False)
            impressora_a_excluir = Impressoras.objects.filter(codigo=codigo)
            impressora_a_excluir.delete()
            messages.success(request, 'Impressora excluída com sucesso! :)')
            Logs.objects.create(acao='Exclusão de impressora', data=datetime.now(), descricao=
                'Foi realizada a exclusão da impressora cujo código de indentificação é {}'.format(codigo), 
                usuario=str(request.user)
                ).save(),
            return redirect('index')
        

        if funcao == 'adiciona_toner':
            quantidade_fornecida = request.POST.get('quantidade', False)
            ticket = request.POST.get('ticket', False)
            
            if solicitacoes.objects.filter(ticket=ticket).exists():
                if solicitacoes.objects.filter(ticket=ticket)[0].status_aberto == False:
                    messages.error(request, 'Este chamado já foi encerrado por {}'.format(str(solicitacoes.objects.filter(ticket=ticket)[0].encerrado_por)))
                    return redirect('index')
                impressora = solicitacoes.objects.filter(ticket=ticket)[0].impressora
                quantidade_antiga = Impressoras.objects.filter(codigo=impressora)[0].qtd_toners
                quantidade_nova = int(quantidade_antiga) + int(quantidade_fornecida)
            else:
                messages.error(request, 'Não há nenhum chamado em aberto com o ticket informado :(')
                return redirect('index')
            if int(quantidade_fornecida) < 1:
                messages.error(request, 'A quantidade de toners novos não pode ser menor que 1 :(')
                return redirect('index')
            if int(quantidade_fornecida) > 1:
                messages.success(request, 'A impressora de código {} ganhou mais {} toners :)'.format(impressora, quantidade_fornecida))
                Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
                Logs.objects.create(acao='Entrada de toner', data=datetime.now(), descricao=
                'Foi realizada a entrada de {} toners para a impressora cujo código de identificação é {}'.format(quantidade_fornecida, impressora), 
                usuario=str(request.user)
                ).save(),
                return redirect('index')
            else:
                messages.success(request, 'A impressora de código {} ganhou mais {} toner :)'.format(impressora, quantidade_fornecida))
                Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
                solicitacoes.objects.filter(ticket=ticket).update(status_aberto=False, encerrado_por=request.user)
                Logs.objects.create(acao='Entrada de toner', data=datetime.now(), descricao=
                'Foi realizada a entrada de {} toner para a impressora cujo código de identificação é {}'.format(quantidade_fornecida, impressora), 
                usuario=str(request.user)
                ).save(),
                return redirect('index')
            
    
        if funcao == 'remove_toner':
            quantidade_fornecida = request.POST.get('quantidade', False)
            impressora = request.POST.get('impressora', False)
            ticket = request.POST.get('ticket', False)
            quantidade_antiga = Impressoras.objects.filter(codigo=impressora)[0].qtd_toners
            quantidade_nova = int(quantidade_antiga) - int(quantidade_fornecida)
            
            if solicitacoes.objects.filter(ticket=ticket).exists() == True:
                messages.error(request, 'Já há uma solicitação com este ticket :(')
                return redirect('index')
            if int(quantidade_nova) < 0:
                messages.error(request, 'A quantidade de saída não pode ser maior que a quantidade atual de toners :(')
                return redirect('index')
            if int(quantidade_fornecida) < 1:
                messages.error(request, 'A quantidade de toners usados não pode ser menor que 1 :(')
                return redirect('index')
            if int(quantidade_fornecida) > 1:
                messages.success(request, 'A impressora de código {} usou mais {} toners :)'.format(impressora, quantidade_fornecida))
                Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
                Logs.objects.create(acao='Saída de toner', data=datetime.now(), descricao=
                'Foi realizada a saída de {} toners para a impressora cujo código de identificação é {}'.format(quantidade_fornecida, impressora), 
                usuario=str(request.user)
                ).save(),
                return redirect('index')
            else:
                messages.success(request, 'A impressora de código {} usou mais {} toner :)'.format(impressora, quantidade_fornecida))
                Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
                solicitacoes.objects.create(
                    usuario=str(request.user), 
                    ticket=ticket, 
                    impressora=impressora, 
                    marca=Impressoras.objects.filter(codigo=impressora)[0].marca,
                    modelo=Impressoras.objects.filter(codigo=impressora)[0].modelo,
                    quantidade=quantidade_fornecida,
                    status_aberto=True,
                    data=datetime.now()
                    ).save()
                Logs.objects.create(acao='Saída de toner', data=datetime.now(), descricao=
                'Foi realizada a saída de {} toner para a impressora cujo código de identificação é {}'.format(quantidade_fornecida, impressora), 
                usuario=str(request.user)
                ).save(),
                return redirect('index')

    dados = {
        'impressoras': Impressoras.objects.all(),
        'iniciais': str(str(request.user))[0]
    }
    if request.user.is_authenticated:
        return render(request, 'app/impressoras.html', dados)
    else:
        return redirect('login')


def logs(request):
    dados = {
        'logs': Logs.objects.all(),
        'iniciais': str(str(request.user))[0],
        'impressoras': Impressoras.objects.all()
    }
    if request.user.is_authenticated:
        return render(request, 'app/logs.html', dados)
    else:
        return redirect('login')

def logs_entrada_toner(request):
    if request.user.is_authenticated:
        dados = {
        'logs': Logs.objects.all(),
        'iniciais': str(str(request.user))[0],
        'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/logs_entrada_toner.html', dados)
    else:
        return redirect('login')

def logs_saida_toner(request):
    if request.user.is_authenticated:
        dados = {
        'logs': Logs.objects.all(),
        'iniciais': str(str(request.user))[0],
        'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/logs_saida_toner.html', dados)
    else:
        return redirect('login')

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


def todas_as_solicitacoes(request):
    if request.user.is_authenticated:
        dados = {
            'solicitacoes': solicitacoes.objects.all(),
            'iniciais': str(request.user)[0],
            'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/todas_as_solicitacoes.html', dados)
    else:
        return redirect('login')

def solicitacoes_em_aberto(request):
    if request.user.is_authenticated:
        dados = {
            'solicitacoes_em_aberto': solicitacoes.objects.filter(status_aberto=True),
            'iniciais': str(request.user)[0],
            'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/solicitacoes_em_aberto.html', dados)
    else:
        return redirect('login')

def solicitacoes_encerradas(request):
    if request.user.is_authenticated:
        dados = {
            'solicitacoes_encerradas': solicitacoes.objects.filter(status_aberto=False),
            'iniciais': str(request.user)[0],
            'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/solicitacoes_encerradas.html', dados)
    else:
        return redirect('login')

def minhas_solicitacoes(request):
    if request.user.is_authenticated:
        dados = {
            'solicitacoes': solicitacoes.objects.filter(usuario=str(request.user)),
            'iniciais': str(request.user)[0],
            'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/minhas_solicitacoes.html', dados)
    else:
        return redirect('login')