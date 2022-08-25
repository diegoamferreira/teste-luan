from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Cliente
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, TemplateView


class ClienteList(ListView):
   model = Cliente
   #template_name ='cliente_list.html'
   paginate_by = 3

class ClienteCreate(CreateView):
   model = Cliente
   success_url = reverse_lazy ('class:urls')
  # template_name = 'create.html'
   fields = '__all__'

class ClienteDetail(DetailView):
   model = Cliente

class ClienteDelete(DeleteView):
   queryset = Cliente.objects.all()
   success_url = reverse_lazy('class:urls')

class ClienteUpdate(UpdateView):
   model = Cliente
   success_url = reverse_lazy('class:urls')
   #template_name = 'create.html'
   fields = '__all__'









