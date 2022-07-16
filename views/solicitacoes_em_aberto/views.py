from django.shortcuts import render, redirect
from app.models import Impressoras, solicitacoes


def solicitacoes_em_aberto(request):
    if request.user.is_authenticated:
        dados = {
            'solicitacoes_em_aberto': solicitacoes.objects.filter(status_aberto=True),
            'iniciais': str(request.user)[0],
            'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/solicitacoes_em_aberto.html', dados)
    else:
        return redirect('login')