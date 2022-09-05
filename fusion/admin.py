from django.contrib import admin
from django.contrib.admin import display

from .models import Empresa, Service, Resource, Team, Plan, Speech, Contact, Phone


#from luan_teste.admin_site import custom_admin_site


@admin.register(Empresa,Resource,Speech,Contact,Phone)
class FusionAdmin(admin.ModelAdmin):
      pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
      list_filter = ["titulo","descricao","empresa__cidade"]
      list_display = ["id","titulo","descricao","get_empresaNome","icone"]
      list_editable = ["titulo","icone"]
      list_display_links = ["id"]
      # list_per_page = 1
      list_max_show_all = 10
      list_select_related = True
      search_fields = ["titulo"]
      search_help_text = "Digite aquei"
      # date_hierarchy = None
      save_as = True
      save_as_continue = True
      # save_on_top = True


      @display(description="Empresa")
      def get_empresaNome(self,obj):
            return obj.empresa.nome

@admin.register(Plan)
class ServiceAdmin(admin.ModelAdmin):
      list_display = ["id","icone"]
      list_editable = ["icone"]

@admin.register(Team)
class ServiceAdmin(admin.ModelAdmin):
      list_filter = ["experiencia"]


