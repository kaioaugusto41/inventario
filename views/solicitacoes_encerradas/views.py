from django.shortcuts import render, redirect
from app.models import Impressoras, solicitacoes

def solicitacoes_encerradas(request):
    if request.user.is_authenticated:
        dados = {
            'solicitacoes_encerradas': solicitacoes.objects.filter(status_aberto=False),
            'iniciais': str(request.user)[0],
            'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/solicitacoes_encerradas.html', dados)
    else:
        return redirect('login')