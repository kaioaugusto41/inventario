from django.shortcuts import render, redirect
from app.models import Impressoras, solicitacoes


def todas_as_solicitacoes(request):
    if request.user.is_authenticated:
        dados = {
            
            'solicitacoes': solicitacoes.objects.all(),
            'iniciais': str(request.user)[0],
            'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/todas_as_solicitacoes.html', dados)
    else:
        return redirect('login')