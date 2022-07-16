from django.shortcuts import render, redirect
from app.models import Impressoras, Logs


def logs(request):
    dados = {
        'logs': Logs.objects.all(),
        'iniciais': str(str(request.user))[0],
        'impressoras': Impressoras.objects.all()
    }
    if request.user.is_authenticated:
        return render(request, 'app/logs.html', dados)
    else:
        return redirect('login')