from django.urls import path

from htmx.views import ServiceListView
import htmx.views as v

urlpatterns = [
    path('service-list', ServiceListView.as_view(), name='service_list'),
    path('services', v.service_base_view, name='service_list'),
    path('service_table', v.service_table_htmx, name='service_table'),
    path('service_create', v.service_create_htmx, name='service_create'),
    path('<int:pk>/service_delete', v.service_delete_htmx, name='service_delete'),
    path('<int:pk>/service_result', v.service_result_view, name='service_result'),
    path('<int:pk>/service_update', v.service_update, name='service_update'),
    path('<int:pk>/service_detail', v.service_detail, name='service_detail'),
]
