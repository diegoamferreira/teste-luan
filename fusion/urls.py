from . import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.checks import templates
from django.urls import include, path

app_name = 'site' #começo da url

urlpatterns = [
    path('home/', views.PaginaInicial.as_view(), name='inicial'),
    path('contact/', login_required(views.ContactCreate.as_view()), name='contact'),
    path('service/detail/<int:pk>/', login_required(views.ServiceDetail.as_view()), name='service_detail'),
    path('resource/detail/<int:pk>/', login_required(views.ResourceDetail.as_view()), name='resource_detail'),
    path('team/detail/<int:pk>/', login_required(views.TeamDetail.as_view()), name='team_detail'),
    path('speech/detail/<int:pk>/', login_required(views.SpeechDetail.as_view()), name='speech_detail'),
    path('plan/detail/<int:pk>/', login_required(views.PlanDetail.as_view()), name='plan_detail'),
    path('phone/', login_required(views.PhoneList.as_view()), name='phone'),
    path('used/', login_required(views.Service_1.as_view()), name='used'),


]