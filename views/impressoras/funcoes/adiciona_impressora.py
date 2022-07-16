from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect
from app.models import Impressoras, Logs



def adiciona_impressora(lista_codigos, lista_ips, codigo, setor, marca, modelo, toners_estoque, ip, request):
    # Valida existência do código
    if codigo in lista_codigos:
        messages.error(request, 'Não foi possível adicionar a impressora pois já existe uma com este código :(')
        return redirect('impressoras')

    # Valida existência do ip
    if ip in lista_ips:
        messages.error(request, 'Não foi possível adicionar a impressora pois já existe uma com este endereço IP :(')
        return redirect('impressoras')

    # Valida tamanho do ip
    if len(ip) < 10 or ip.count('.') != 3:
        messages.error(request, 'O endereço IP {} não é um IP válido :('.format(ip))
        return redirect('impressoras')
    
    # ADICIONA A IMPRESSORA
    else:
        impressora_nova = Impressoras.objects.create(
                    codigo=codigo,
                    setor=setor, 
                    marca=marca, 
                    modelo=modelo, 
                    qtd_toners=toners_estoque, 
                    ip=ip, 
                    status=False
                    )     
        impressora_nova.save()
        messages.success(request, 'Impressora salva com sucesso! :)')
        Logs.objects.create(acao='Cadastro de impressora', data=datetime.now(), descricao=
        'Foi realizado o cadastro de uma nova impressora, cujo código de identificação é {}'.format(codigo), 
        usuario=str(request.user)
        ).save(),
        return redirect('impressoras')