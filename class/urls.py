from . import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.checks import templates
from django.urls import include, path

app_name = 'class' #começo da url

urlpatterns = [
    path('classlist/', views.ClienteList.as_view(), name='urls'),
    path('create/', views.ClienteCreate.as_view(), name='list_create'),
    path('detail/<int:pk>/', views.ClienteDetail.as_view(), name='list_detail'),
    path('delete/<int:pk>/', views.ClienteDelete.as_view(), name='list_delete'),
    path('update/<int:pk>/', views.ClienteUpdate.as_view(), name='list_update'),


 ]
