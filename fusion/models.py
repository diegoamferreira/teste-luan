from django.contrib.auth.models import User
from django.db import models

#Create your models here.
# class Fusion(models.Model):
#     servico = models.CharField(max_length=100)
#     titulo = models.CharField(max_length=100)
#     descricao = models.TextField(blank=True, null=True)
    # data_tempo = models.DateTimeField(verbose_name='Data do Evento')
    # data_dia = models.DateField(verbose_name='Data do Evento')
    # salario = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    # habilitado = models.BooleanField(default=True, blank=True)
    # data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE) #relacionameto com outra tabela

 # #  def __str__(self):
 #       return self.titulo

class Empresa(models.Model):
    nome  = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100,blank=True, null=True)
    estado = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f'{self.nome} | {self.cidade} - {self.estado}'


class Service(models.Model):
     titulo = models.CharField(max_length=100)
     descricao = models.TextField(blank=True, null=True)
     icone = models.CharField(max_length=100)
     empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE) #relaciona o registro da tabela com o registro da tabela  Empresa

     class Meta:
         verbose_name = 'Serviço'
         verbose_name_plural = 'Serviços'

     def __str__(self):
         return self.titulo