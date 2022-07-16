from django.shortcuts import render, redirect
from app.models import Impressoras, Logs

def logs_entrada_toner(request):
    if request.user.is_authenticated:
        dados = {
            
        'logs': Logs.objects.all(),
        'iniciais': str(str(request.user))[0],
        'impressoras': Impressoras.objects.all()
        }
        return render(request, 'app/logs_entrada_toner.html', dados)
    else:
        return redirect('login')