

from datetime import datetime
from django.shortcuts import redirect
from app.models import Impressoras, Logs, solicitacoes
from django.contrib import messages


def adiciona_toner(quantidade_fornecida, ticket, request):
    if ticket.lstrip() == '':
        messages.error(request, 'O campo ticket não pode ficar em branco :(')
        return redirect('index')

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
        solicitacoes.objects.filter(ticket=ticket).update(status_aberto=False, encerrado_em=datetime.now(), encerrado_por=str(request.user))
        Logs.objects.create(acao='Entrada de toner', data=datetime.now(), descricao=
        'Foi realizada a entrada de {} toners para a impressora cujo código de identificação é {}'.format(quantidade_fornecida, impressora), 
        usuario=str(request.user)
        ).save(),
        return redirect('index')
    else:
        messages.success(request, 'A impressora de código {} ganhou mais {} toner :)'.format(impressora, quantidade_fornecida))
        Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
        solicitacoes.objects.filter(ticket=ticket).update(status_aberto=False, encerrado_em=datetime.now(), encerrado_por=str(request.user))
        Logs.objects.create(acao='Entrada de toner', data=datetime.now(), descricao=
        'Foi realizada a entrada de {} toner para a impressora cujo código de identificação é {}'.format(quantidade_fornecida, impressora), 
        usuario=str(request.user)
        ).save(),
        return redirect('index')