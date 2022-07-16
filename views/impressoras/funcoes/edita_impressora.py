from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect
from app.models import Logs


def edita_impressora(lista_ips, codigo, setor, marca, modelo, toners_estoque, ip, impressora_a_editar, impressora_a_editar_ip, request):

    # Valida existência do ip
    if ip != impressora_a_editar_ip and ip in lista_ips:
        messages.error(request, 'Não foi possível editar a impressora pois já existe uma com este endereço IP :(')
        return redirect('impressoras')

    # Valida tamanho do ip
    if len(ip) < 10 or ip.count('.') != 3:
        messages.error(request, 'O endereço IP {} não é um IP válido :('.format(ip))
        return redirect('impressoras')
        
    impressora_a_editar.update(codigo=codigo, setor=setor, marca=marca, modelo=modelo, qtd_toners=toners_estoque, ip=ip)
    if codigo != False:
        messages.success(request, 'Impressora editada com sucesso! :)')
        Logs.objects.create(acao='Edição de impressora', data=datetime.now(), descricao=
        'Foi realizada alterações na impressora cujo código de indentificação é {}'.format(codigo), 
        usuario=str(request.user)
        ).save(),
        return redirect('impressoras')