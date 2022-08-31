from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from .models import Service, Resource, Team, Plan, Speech, Contact,Phone
from .forms import ContactForm


class PaginaInicial(TemplateView):
    template_name = 'fusion.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        empresa = user.empresa
        context = super(PaginaInicial, self).get_context_data()
        services = Service.objects.filter(empresa=empresa)
        context["services"] = services
        #            resources = Resource.objects.all()
        #            context["resources"] = resources
        resources = Resource.objects.filter(empresa=empresa)
        context["resources"] = resources
        #            teams = Team.objects.all()
        #            context["teams"] = teams
        teams = Team.objects.filter(empresa=empresa)
        context["teams"] = teams
        plans = Plan.objects.filter(empresa=empresa)
        context["plans"] = plans
        speechs = Speech.objects.filter(empresa=empresa)
        context["speechs"] = speechs
        form = ContactForm
        context["form"] = form
        return context


class Service_1(TemplateView):
    template_name = 'partials/service1.html'


class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('site:contact')
    template_name = 'partials/contact.html'

    # fields = '__all__'

    def form_valid(self, form):
        user = self.request.user
        empresa = user.empresa
        form.instance.empresa = empresa
        return super().form_valid(form)


class ServiceDetail(DetailView):
    model = Service
    template_name = 'details/service_detail.html'

    def get(self, request, *args, **kwargs):
        usuario = request.user
        service = self.get_object()
        usuario_service = service.empresa.usuario

        if usuario != usuario_service:
            return HttpResponse(status=401, content="Voce não tem acesso a esse produto")
        return super().get(self, request, *args, **kwargs)

class ResourceDetail(DetailView):
    model = Resource
    template_name = 'details/resource_detail.html'

    def get(self, request, *args, **kwargs):
        usuario = request.user
        resource = self.get_object()
        usuario_resource = resource.empresa.usuario

        if usuario != usuario_resource:
            return HttpResponse(status=401, content="Voce não tem acesso a esse produto")
        return super().get(self, request, *args, **kwargs)

class TeamDetail(DetailView):
    model = Team
    template_name = 'details/team_detail.html'

    def get(self, request, *args, **kwargs):
        usuario = request.user
        team = self.get_object()
        usuario_team = team.empresa.usuario

        if usuario != usuario_team:
            return HttpResponse(status=401, content="Voce não tem acesso a essa conta")
        return super().get(self, request, *args, **kwargs)

class SpeechDetail(DetailView):
    model = Speech
    template_name = 'details/speech_detail.html'

    def get(self, request, *args, **kwargs):
        usuario = request.user
        speech = self.get_object()
        usuario_speech = speech.empresa.usuario

        if usuario != usuario_speech:
            return HttpResponse(status=401, content="Voce não tem acesso a essa conta")
        return super().get(self, request, *args, **kwargs)

class PlanDetail(DetailView):
    model = Plan
    template_name = 'details/plan_detail.html'

    def get(self, request, *args, **kwargs):
        usuario = request.user
        plan = self.get_object()
        usuario_plan = plan.empresa.usuario

        if usuario != usuario_plan:
            return HttpResponse(status=401, content="Voce não tem acesso a essa conta")
        return super().get(self, request, *args, **kwargs)

class PhoneList(ListView):
   model = Phone
   template_name ='partials/phone.html'
   paginate_by = 3
