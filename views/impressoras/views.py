from datetime import datetime
from os import remove
from django.contrib import messages
from django.shortcuts import render, redirect
from app.models import Impressoras, Logs, solicitacoes
from views.impressoras.funcoes.adiciona_toner import adiciona_toner
from views.impressoras.funcoes.exclui_impressora import exclui_impressora
from views.impressoras.funcoes.adiciona_impressora import adiciona_impressora
from views.impressoras.funcoes.edita_impressora import edita_impressora
from views.impressoras.funcoes.remove_toner import remove_toner

def impressoras(request):

    lista_codigos = []
    lista_ips = []
    for impressora in Impressoras.objects.all():
        lista_codigos.append(str(impressora.codigo))
        lista_ips.append(str(impressora.ip))

    if request.method == 'GET':
        funcao = request.GET.get('funcao')
        
        if funcao == 'edita_impressora':

            # DADOS RECEBIDOS DO TEMPLATE
            codigo = request.GET.get('codigo', False)
            setor = request.GET.get('setor', False)
            marca = request.GET.get('marca', False)
            modelo = request.GET.get('modelo', False)
            toners_estoque = request.GET.get('toners_estoque', False)
            ip = request.GET.get('ip', False)
            impressora_a_editar = Impressoras.objects.filter(codigo=codigo)
            impressora_a_editar_ip = str(Impressoras.objects.filter(codigo=codigo)[0].ip)

            # FUNÇÃO RESPONSÁVEL POR EDITAR A IMPRESSORA
            edita_impressora(lista_ips, codigo, setor, marca, modelo, toners_estoque, ip, impressora_a_editar, impressora_a_editar_ip, request)
            return redirect('impressoras')


    if request.method == 'POST':
        funcao = request.POST.get('funcao')

        if funcao == 'adiciona_impressora':

            # DADOS RECEBIDOS DO TEMPLATE
            codigo = request.POST.get('codigo', False).upper()
            setor = request.POST.get('setor', False).title()
            marca = request.POST.get('marca', False).title()
            modelo = request.POST.get('modelo', False).upper()
            toners_estoque = request.POST.get('toners_estoque', False)
            ip = request.POST.get('ip', False)

            # FUNÇÃO RESPONSÁVEL POR ADICIONAR IMPRESSORAS    
            adiciona_impressora(lista_codigos, lista_ips, codigo, setor, marca, modelo, toners_estoque, ip, request)
            return redirect('impressoras')

        if funcao == 'exclui_impressora':

            # DADOS RECEBIDOS DO TEMPLATE
            codigo = request.POST.get('codigo', False)
            impressora_a_excluir = Impressoras.objects.filter(codigo=codigo)
            
            # FUNÇÃO RESPONSÁVEL POR EXCLUIR IMPRESSORAS
            exclui_impressora(codigo, impressora_a_excluir, request)
            return redirect('impressoras')       

        if funcao == 'adiciona_toner':
            quantidade_fornecida = request.POST.get('quantidade', False)
            ticket = request.POST.get('ticket', False)
            
            adiciona_toner(quantidade_fornecida, ticket, request)
            return redirect('index')
            
        if funcao == 'remove_toner':
            quantidade_fornecida = request.POST.get('quantidade', False)
            impressora = request.POST.get('impressora', False)
            ticket = request.POST.get('ticket', False)
            marca = Impressoras.objects.filter(codigo=impressora)[0].marca
            modelo = Impressoras.objects.filter(codigo=impressora)[0].modelo
            setor = Impressoras.objects.filter(codigo=impressora)[0].setor 
            quantidade_antiga = Impressoras.objects.filter(codigo=impressora)[0].qtd_toners
            quantidade_nova = int(quantidade_antiga) - int(quantidade_fornecida)
            
            remove_toner(impressora, quantidade_nova, quantidade_fornecida, ticket, marca, modelo, setor, request)
            return redirect('index')
    
    dados = {      
            'impressoras': Impressoras.objects.all(),
            'iniciais': str(str(request.user))[0]
        }
    
    if request.user.is_authenticated:
        return render(request, 'app/impressoras.html', dados)
    else:
        return redirect('login')