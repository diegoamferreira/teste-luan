from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from core.views import besta, HomeView, ListHomeView  # HomeView

urlpatterns = [
    # path('', login_required(HomeView.as_view()), name='home'),
    path('', login_required(ListHomeView.as_view()), name='home'),
    # path('', login_required(besta), name='home'),
    # path('admin/', login_required(HomeView.as_view()), name='home'),
    # path('accounts/', include('allauth.urls')),
    # path('3', login_required(HomeView.as_view()), name='home'),
    # path('4', login_required(HomeView.as_view()), name='home'),
    # path('', HomeView.as_view(), name='home'),
]

# path('', login_required(v.list_produtos_page), name='produto_mp_list'),
