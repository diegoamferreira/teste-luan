from django.contrib import admin
from .models import Eventos

# Register your models here.
class EventosAdmin (admin.ModelAdmin) :
    list_display = ('pk', 'titulo', 'data_criacao', 'descricao', 'data_evento', 'salario', 'habilitado')
    list_filter = ('titulo',)#'data_evento')

admin.site.register(Eventos, EventosAdmin)