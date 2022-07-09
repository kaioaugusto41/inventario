from django.contrib import messages
import imp
from django.shortcuts import render, redirect
from app.models import Impressoras
from views.index.funcoes.adiciona_impressora import adiciona_impressora


def index(request):

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
            if len(ip) > 12 or len(ip) < 10 or ip.count('.') != 3:
                messages.error(request, 'O endereço IP {} não é um IP válido :('.format(ip))
                return redirect('index')
            
            # ADICIONA A IMPRESSORA
            else:
                adiciona_impressora(request, codigo, setor, marca, modelo, toners_estoque, ip)



        if funcao == 'exclui_impressora':
            codigo = request.POST.get('codigo', False)
            impressora_a_excluir = Impressoras.objects.filter(codigo=codigo)
            impressora_a_excluir.delete()
            messages.success(request, 'Impressora excluída com sucesso! :)')
            return redirect('index')
        

    dados = {
        'impressoras': Impressoras.objects.all()
    }
    return render(request, 'index.html', dados)