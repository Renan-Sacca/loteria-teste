from django.db import models
class skin(models.Model):
    nome = models.CharField(max_length=200)
    categoria =  models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    link = models.TextField()

class rifa(models.Model):
    valor_total = models.DecimalField(max_digits=7, decimal_places=2)
    num_entradas = models.IntegerField()
    valor_entrada = models.IntegerField()
    participantes = models.TextField()
    data_inicial = models.DateField()
    data_final =  models.DateField()
    skin = models.ForeignKey(skin,on_delete=models.CASCADE)
    ativa = models.BooleanField()


class historico(models.Model):
    nome_vencedor = models.CharField(max_length=200)
    data_sorteio =   models.DateField()
    id_vencedor = models.IntegerField()
    skin =  models.IntegerField()

