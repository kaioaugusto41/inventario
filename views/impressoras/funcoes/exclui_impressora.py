from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect
from app.models import Logs

def exclui_impressora(codigo, impressora_a_excluir, request):
    impressora_a_excluir.delete()
    messages.success(request, 'Impressora excluída com sucesso! :)')
    Logs.objects.create(acao='Exclusão de impressora', data=datetime.now(), descricao=
        'Foi realizada a exclusão da impressora cujo código de indentificação é {}'.format(codigo), 
        usuario=str(request.user)
        ).save(),
    return redirect('impressoras')