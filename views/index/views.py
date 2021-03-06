from django.shortcuts import render, redirect
from app.models import Impressoras, solicitacoes



def index(request):

    if request.user.is_authenticated:
        print(solicitacoes.objects.all())

        dados = {
            'solicitacoes_em_aberto': solicitacoes.objects.filter(status_aberto=True),
            'iniciais': str(str(request.user))[0],
            'impressoras': Impressoras.objects.all()
        }  
        return render(request, 'app/index.html', dados)

    else:
        return redirect('login')






