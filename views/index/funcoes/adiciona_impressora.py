from django.shortcuts import redirect
from app.models import Impressoras
from django.contrib import messages

def adiciona_impressora(request, codigo, setor, marca, modelo, toners_estoque, ip):
    impressora_nova = Impressoras.objects.create(
                    codigo=codigo,
                    setor=setor, 
                    marca=marca, 
                    modelo=modelo, 
                    qtd_toners=toners_estoque, 
                    ip=ip, 
                    status=False
                    )     
    impressora_nova.save()
    messages.success(request, 'Impressora salva com sucesso! :)')
    return redirect('index')