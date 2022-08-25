from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from .models import Eventos
from .form import FormEventos
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos_eventos'] = Eventos.objects.all()
        context['teste'] = 'TOP DEMAIS - ' * 20
        return context


class ListHomeView(ListView):
    model = Eventos
    template_name = 'home.html'
    context_object_name = 'todos_eventos'

def evento (request):
    evento_list = Eventos.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(evento_list, 2)
    print('estou aqui')
    try:
        eventos = paginator.page(page)
    except PageNotAnInteger:
        eventos = paginator.page(1)
    except EmptyPage:
        eventos = paginator.page(paginator.num_pages)
    context = {
        'page_obj': eventos
    }
    return render(request,'home.html', context)

def besta(request):
    todos_eventos = Eventos.objects.all()
    contexto = {
        'todos_eventos': todos_eventos,
        'teste': 'TOP DEMAIS - ' * 20
    }

    return render(request, 'home.html', context=contexto)

def evento_add (request):
    form = FormEventos(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        'form':form,
        'titulo_da_pagina':'Criar autor',
        'nome_botao': "Criar"
    }

    return render(request,'index.html', context)

def evento_del (request, pk):
    evento = Eventos.objects.get(pk=pk)
    evento.delete()
    return redirect("home")

def evento_upd (request,pk):
    evento =Eventos.objects.get(pk=pk)
    form = FormEventos(request.POST or None, instance=evento)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        'form': form,
        'titulo_da_pagina': 'Editar autor',
        'nome_botao': "Editar"
    }
    return render(request,'index.html',context)

def evento_view (request, pk):
    evento =Eventos.objects.get(pk=pk)



    context = {
        'evento': evento,
        'titulo_da_pagina': 'Visualizar',
        'nome_botao': "Visualisar"
    }
    return render(request,'preview.html',context)

