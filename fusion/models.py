from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
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
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, blank=True, null=True)
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
    empresa = models.ForeignKey(Empresa,
                                on_delete=models.CASCADE)  # relaciona o registro da tabela com o registro da tabela  Empresa

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.titulo


class Resource(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    icone = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa,
                                on_delete=models.CASCADE)  # relaciona o registro da tabela com o registro da tabela  Empresa

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.titulo


class Team(models.Model):
    CARGOCHOICES = (
        ("1", "Area de programação"),
        ("2", "Area de direito"),
        ("3", "Area de diretoria"),
        ("4", "Area de almoxerifado"),
        ("5", "Area de farmácia"),
    )
    nome = models.CharField(max_length=100)
    cargo = models.CharField(choices=CARGOCHOICES, max_length=2)
    descricao = models.TextField(max_length=100)
    facebook_url = models.EmailField(blank=True, null=True)
    twitter_url = models.EmailField(blank=True, null=True)
    instagran_url = models.EmailField(blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.nome


class Plan(models.Model):
    preco = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    titulo = models.TextField(max_length=100, blank=True, null=True)
    icone = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.preco


class Speech(models.Model):
    imagem = models.ImageField(blank=True, null=True)
    nome = models.TextField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100)
    menssagem = models.TextField(max_length=100)
    nota = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    nota2 = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=0)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.nota


class Contact(models.Model):
    nome = models.TextField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    assunto = models.TextField(max_length=100)
    mensagem = models.TextField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.nome
