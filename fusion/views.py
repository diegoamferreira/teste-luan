from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class PaginaInicial(TemplateView):
   template_name = 'fusion.html'

class Service_1(TemplateView):
   template_name = 'funcion_1/service_1.html'