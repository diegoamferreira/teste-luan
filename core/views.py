from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from core.models import Eventos


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


def besta(request):
    todos_eventos = Eventos.objects.all()
    contexto = {
        'todos_eventos': todos_eventos,
        'teste': 'TOP DEMAIS - ' * 20
    }

    return render(request, 'home.html', context=contexto)
