import imp
import os
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

    # IMPRESSORAS CADASTRADAS
    impressoras = []
    for impressora in Impressoras.objects.all():
        impressoras.append(impressora)
    
    # LISTA DE IPS
    lista_ips = []
    for impressora in impressoras:
        lista_ips.append(str(impressora.ip))


    # PINGA IPS
    lista_pings = []
    for ip in lista_ips:
        response = os.system("ping -n 2 " + ip)
        if response == 0:
            lista_pings.append(True)
        else:
            lista_pings.append(False)

    # LISTAS ZIPADAS
    impressoras_e_pings = zip(impressoras, lista_pings)

    dados = {
        'impressoras_e_pings': impressoras_e_pings
    }
    return render(request, 'index.html', dados)