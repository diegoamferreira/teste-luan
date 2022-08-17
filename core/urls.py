from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from core.views import HomeView

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    # path('', HomeView.as_view(), name='home'),
]


#path('', login_required(v.list_produtos_page), name='produto_mp_list'),
