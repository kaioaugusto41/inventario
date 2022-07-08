from django.shortcuts import render

from app.models import Impressoras

def index(request):
    print(Impressoras.objects.all())
    dados = {
        'impressoras': Impressoras.objects.all()
    }
    return render(request, 'index.html', dados)