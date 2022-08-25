from . import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.checks import templates
from django.urls import include, path

app_name = 'site' #começo da url

urlpatterns = [
    path('home/', views.PaginaInicial.as_view(), name='inicial'),
    path('used/', views.Service_1.as_view(), name='used'),


]