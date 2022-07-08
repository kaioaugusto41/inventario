from django.contrib import messages
import imp
from django.shortcuts import render, redirect

from app.models import Impressoras

def index(request):

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
        codigo = request.POST.get('codigo', False)
        impressora_a_excluir = Impressoras.objects.filter(codigo=codigo)
        impressora_a_excluir.delete()
        messages.success(request, 'Impressora excluída com sucesso! :)')
        return redirect('index')
        

    dados = {
        'impressoras': Impressoras.objects.all()
    }
    return render(request, 'index.html', dados)