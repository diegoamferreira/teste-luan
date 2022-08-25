from . import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.checks import templates
from django.urls import include, path

from .views import besta, HomeView, ListHomeView #HomeView

urlpatterns = [
    #path('', login_required(HomeView.as_view()), name='home'),
    path('', login_required(views.evento), name='home'),
    path('abra/', views.besta, name='todos_eventos'),
    path('<int:pk>/delete', views.evento_del, name='delete_evento'),
    path('l', views.evento_add, name='abra'),
    path('<int:pk>/update', views.evento_upd, name='update_evento'),
    path('<int:pk>/preview', views.evento_view, name='visualizar'),
    # path('3', login_required(HomeView.as_view()), name='home'),
    # path('4', login_required(HomeView.as_view()), name='home'),
    # path('', HomeView.as_view(), name='home'),
]

# path('', login_required(v.list_produtos_page), name='produto_mp_list'),
