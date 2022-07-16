from django.shortcuts import render, redirect
from app.models import Impressoras, solicitacoes

def minhas_solicitacoes(request):
    if request.user.is_authenticated:
        dados = {
            
            'solicitacoes': solicitacoes.objects.filter(usuario=str(request.user)),
            'iniciais': str(request.user)[0],
            'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/minhas_solicitacoes.html', dados)
    else:
        return redirect('login')