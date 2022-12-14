from django.contrib.auth.models import User
from django.db import models

#Create your models here.
class Cliente(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    salario = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    habilitado = models.BooleanField(default=True, blank=True)
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

 # #  def __str__(self):
 #       return self.titulo