from django.db import models

# Create your models here.
class Impressoras(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    setor = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    qtd_toners = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.codigo