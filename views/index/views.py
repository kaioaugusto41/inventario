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
            if len(ip) < 10 or ip.count('.') != 3:
                messages.error(request, 'O endereço IP {} não é um IP válido :('.format(ip))
                return redirect('index')
            
            # ADICIONA A IMPRESSORA
            else:
                adiciona_impressora(request, codigo, setor, marca, modelo, toners_estoque, ip)
                return redirect('index')


        if funcao == 'exclui_impressora':
            codigo = request.POST.get('codigo', False)
            impressora_a_excluir = Impressoras.objects.filter(codigo=codigo)
            impressora_a_excluir.delete()
            messages.success(request, 'Impressora excluída com sucesso! :)')
            return redirect('index')
        

        if funcao == 'adiciona_toner':
            quantidade_fornecida = request.POST.get('quantidade', False)
            impressora = request.POST.get('impressora', False)
            quantidade_antiga = Impressoras.objects.filter(codigo=impressora)[0].qtd_toners
            quantidade_nova = int(quantidade_antiga) + int(quantidade_fornecida)
            if int(quantidade_fornecida) < 1:
                messages.error(request, 'A quantidade de toners novos não pode ser menor que 1 :(')
                return redirect('index')
            if int(quantidade_fornecida) > 1:
                messages.success(request, 'A impressora de código {} ganhou mais {} toners :)'.format(impressora, quantidade_fornecida))
                Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
                return redirect('index')
            else:
                messages.success(request, 'A impressora de código {} ganhou mais {} toner :)'.format(impressora, quantidade_fornecida))
                Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
                return redirect('index')
            
    
        if funcao == 'remove_toner':
            quantidade_fornecida = request.POST.get('quantidade', False)
            impressora = request.POST.get('impressora', False)
            quantidade_antiga = Impressoras.objects.filter(codigo=impressora)[0].qtd_toners
            quantidade_nova = int(quantidade_antiga) - int(quantidade_fornecida)
            
            if int(quantidade_nova) < 0:
                messages.error(request, 'A quantidade de saída não pode ser maior que a quantidade atual de toners :(')
                return redirect('index')
            if int(quantidade_fornecida) < 1:
                messages.error(request, 'A quantidade de toners usados não pode ser menor que 1 :(')
                return redirect('index')
            if int(quantidade_fornecida) > 1:
                messages.success(request, 'A impressora de código {} usou mais {} toners :)'.format(impressora, quantidade_fornecida))
                Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
                return redirect('index')
            else:
                messages.success(request, 'A impressora de código {} usou mais {} toner :)'.format(impressora, quantidade_fornecida))
                Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
                return redirect('index')

    dados = {
        'impressoras': Impressoras.objects.all()
    }
    return render(request, 'app/index.html', dados)