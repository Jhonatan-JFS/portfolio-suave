from django.contrib import admin
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "destaque", "publicado", "criado_em")
    list_filter = ("destaque", "publicado")
    search_fields = ("titulo", "resumo", "tecnologias")
