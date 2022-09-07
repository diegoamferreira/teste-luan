import time

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from fusion.icons import ICONS_CHOICE
from fusion.models import Service
from htmx.forms import ServiceForm


# Create your views here.

class ServiceListView(ListView):
    model = Service
    template_name = 'htmx/service_list.html'
    paginate_by = 3


def service_base_view(request):
    usuarios = User.objects.all()
    template_name = 'htmx/services/service_base.html'
    icones = ICONS_CHOICE
    return render(request, template_name=template_name, context={'icones': icones, 'usuarios': usuarios})


# MAIN VIEW
def service_table_htmx(request):
    # time.sleep(2)
    order_by = request.GET.get('order', '-pk')
    search = request.GET.get('search')
    usuario = request.GET.get('usuario')

    rows_per_page = 3
    services = Service.objects.filter(status='active').order_by(order_by)
    if search:
        services = services.filter(
            Q(titulo__icontains=search) |
            Q(descricao__icontains=search) |
            Q(icone__icontains=search)
        )
    if usuario:
        usuario = User.objects.get(pk=usuario)
        services = services.filter(empresa__usuario=usuario)

    paginator = Paginator(services, rows_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'paginator': paginator,
        'page_obj': page_obj,
        'rows_per_page': rows_per_page,
    }

    template_name = 'htmx/services/service_table.html'
    return render(request, template_name=template_name, context=context)


def service_create_htmx(request):
    # time.sleep(5)
    template_name = 'htmx/services/service_form.html'
    form = ServiceForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            service = form.save()
            # invite = form.save(commit=False)
            # invite.user = request.user
            template_name = 'htmx/services/service_result.html'
            context = {'object': service}
            return render(request, template_name, context)
        return HttpResponse(status=200, content=form.errors.as_ul())

    context = {'form': form, 'create': True}
    return render(request, template_name, context)


def service_update(request, pk):
    obj = Service.objects.get(pk=pk)
    form = ServiceForm(request.POST or None, instance=obj)
    template_name = 'htmx/services/service_form.html'

    if request.method == 'POST':
        if form.is_valid():
            service = form.save()
            template_name = 'htmx/services/service_result.html'
            context = {'object': service}
            return render(request, template_name, context)
        return HttpResponse(status=200, content=form.errors.as_ul())

    context = {
        'form': form,
        'create': False,
        'object': obj
    }
    return render(request, template_name, context)


def service_result_view(request, pk):
    # print(dir(request))
    # if 'Hx-Request' in request.headers:
    #     hx = request.headers['Hx-Request']
    #     print('SOU UMA REQUISIÇÃO DO HTMX')
    #     print(hx)
    # else:
    #     print('EU NÃO')
    if 'Hx-Request' not in request.headers:
        return HttpResponse(status=404)

    obj = Service.objects.get(pk=pk)
    template_name = 'htmx/services/service_result.html'
    context = {'object': obj}
    return render(request, template_name, context)


@require_http_methods(['DELETE'])
def service_delete_htmx(request, pk):
    print('DELETE CLICADO')
    obj = Service.objects.get(pk=pk)
    # if obj.empresa.usuario == request.user:
    obj.status = 'deleted'
    obj.save()
    return HttpResponse(status=200)
    # return HttpResponse(content='VOCÊ NÃO É O DONO DESSE SERVIÇO')


#  DELETE EXCLUINDO O PRODUTO E VERIFANCO SE O USUARIO É O DONO
# @require_http_methods(['DELETE'])
# def service_delete_htmx(request, pk):
#     print('DELETE CLICADO')
#     obj = Service.objects.get(pk=pk)
#     if obj.empresa.usuario == request.user:
#         obj.delete()
#         return HttpResponse(status=200)
#     return HttpResponse(content='VOCÊ NÃO É O DONO DESSE SERVIÇO')


def service_detail(request, pk):
    obj = Service.objects.get(pk=pk)
    template_name = 'htmx/services/service_detail.html'

    context = {
        'object': obj
    }
    return render(request, template_name, context)
