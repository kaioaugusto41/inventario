

from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from app.models import Impressoras, Logs, solicitacoes


def remove_toner(impressora, quantidade_nova, quantidade_fornecida, ticket, marca, modelo, setor, request):
    if ticket.lstrip() == '':
        messages.error(request, 'O campo ticket não pode ficar em branco :(')
        return redirect('index')
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
        send_mail(
            'Resposição de Toner - Nova Motores e Fios',
            ' Olá, tudo bem? Essa é uma mensagem automática de solicitação de toner. Segue abaixo informações da solicitação: \n \n Código da impressora: {} \n Marca: {} \n Modelo: {} \n Setor: {} \n Quantidade de toners solicitada: {} \n Solicitante: {} \n Chamado interno: {} \n \n Agradecemos, atenciosamente Grupo Nova :)'.format(impressora, marca, modelo, setor, quantidade_fornecida, str(request.user), ticket),
            'atendimento@novafund.com.br',
            ['kaioaugusto41@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'A impressora de código {} usou mais {} toners :)'.format(impressora, quantidade_fornecida))
        Impressoras.objects.filter(codigo=impressora).update(qtd_toners=quantidade_nova)
        solicitacoes.objects.create(
            usuario=str(request.user), 
            ticket=ticket, 
            impressora=impressora, 
            marca=Impressoras.objects.filter(codigo=impressora)[0].marca,
            modelo=Impressoras.objects.filter(codigo=impressora)[0].modelo,
            quantidade=quantidade_fornecida,
            status_aberto=True,
            data=datetime.now(),
            encerrado_em=datetime.now()
            ).save(),
            
        Logs.objects.create(acao='Saída de toner', data=datetime.now(), descricao=
        'Foi realizada a saída de {} toners para a impressora cujo código de identificação é {}'.format(quantidade_fornecida, impressora), 
        usuario=str(request.user)
        ).save(),
        return redirect('index')
    else:
        send_mail(
            'Resposição de Toner - Nova Motores e Fios',
            ' Olá, tudo bem? Essa é uma mensagem automática de solicitação de toner. Segue abaixo informações da solicitação: \n \n Código da impressora: {} \n Marca: {} \n Modelo: {} \n Setor: {} \n Quantidade de toners solicitada: {} \n Solicitante: {} \n Chamado interno: {} \n \n Agradecemos, atenciosamente Grupo Nova :)'.format(impressora, marca, modelo, setor, quantidade_fornecida, str(request.user), ticket),
            'atendimento@novafund.com.br',
            ['kaioaugusto41@gmail.com'],
            fail_silently=False,
        )
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
            data=datetime.now(),
            encerrado_em=datetime.now()
            ).save()
        Logs.objects.create(acao='Saída de toner', data=datetime.now(), descricao=
        'Foi realizada a saída de {} toner para a impressora cujo código de identificação é {}'.format(quantidade_fornecida, impressora), 
        usuario=str(request.user)
        ).save(),
        return redirect('index')

        
