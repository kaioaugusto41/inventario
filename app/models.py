from django.db import models

# Create your models here.
class Impressoras(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    setor = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    qtd_toners = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.codigo

class Logs(models.Model):
    acao = models.CharField(max_length=100)
    data = models.DateTimeField()
    descricao = models.TextField()
    usuario = models.CharField(max_length=200)
    ticket = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.acao

class solicitacoes(models.Model):
    usuario = models.CharField(max_length=50)
    ticket = models.CharField(max_length=100)
    impressora = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    status_aberto = models.BooleanField(default=True)
    data = models.DateTimeField()
    encerrado_em = models.DateTimeField(blank=True)
    encerrado_por = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.ticket