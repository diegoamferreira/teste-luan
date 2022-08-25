from django.contrib import admin
from .models import Cliente


#Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'titulo', 'data_criacao', 'descricao', 'data_evento', 'salario', 'habilitado')
    list_filter = ('titulo',)  # 'data_evento')


admin.site.register(Cliente, ClienteAdmin)
from django.contrib import admin

# Register your models here
