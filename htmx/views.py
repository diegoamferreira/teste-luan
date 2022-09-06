import time

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from fusion.models import Service
from htmx.forms import ServiceForm


# Create your views here.

class ServiceListView(ListView):
    model = Service
    template_name = 'htmx/service_list.html'
    paginate_by = 3


def service_base_view(request):
    template_name = 'htmx/service_base.html'
    return render(request, template_name=template_name)


def service_table_htmx(request):
    # time.sleep(2)
    order_by = request.GET.get('order', '-pk')

    rows_per_page = 3
    services = Service.objects.all().order_by(order_by)
    paginator = Paginator(services, rows_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'paginator': paginator,
        'page_obj': page_obj,
        'rows_per_page': rows_per_page
    }

    template_name = 'htmx/services/service_table.html'
    return render(request, template_name=template_name, context=context)


def service_create_htmx(request):
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

    context = {'form': form}
    return render(request, template_name, context)


@require_http_methods(['DELETE'])
def service_delete_htmx(request, pk):
    print('DELETE CLICADO')
    obj = Service.objects.get(pk=pk)
    if obj.empresa.usuario == request.user:
        obj.delete()
        return HttpResponse(status=200)
    return HttpResponse(content='VOCÊ NÃO É O DONO DESSE SERVIÇO')
