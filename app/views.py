import imp
from django.shortcuts import render

from app.models import Impressoras

def index(request):

    # EDITA AS IMPRESSORAS
    if request.method == 'GET':
        codigo = request.GET.get('codigo', False)
        setor = request.GET.get('setor', False)
        marca = request.GET.get('marca', False)
        modelo = request.GET.get('modelo', False)
        toners_estoque = request.GET.get('toners_estoque', False)
        ip = request.GET.get('ip', False)
        impressora_a_editar = Impressoras.objects.filter(codigo=codigo)
        impressora_a_editar.update(codigo=codigo, setor=setor, marca=marca, modelo=modelo, qtd_toners=toners_estoque, ip=ip)

        

    dados = {
        'impressoras': Impressoras.objects.all()
    }
    return render(request, 'index.html', dados)