from django.contrib import admin

from .models import Area, Trilha, TrilhaCurso


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ["nome", "icone", "cor", "ativa", "data_criacao"]
    list_filter = ["ativa", "data_criacao"]
    search_fields = ["nome", "descricao"]
    ordering = ["nome"]


@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    list_display = ["titulo", "usuario", "area", "ativa", "data_criacao"]
    list_filter = ["ativa", "area", "data_criacao"]
    search_fields = ["titulo", "descricao", "usuario__nome"]
    ordering = ["-data_criacao"]
    raw_id_fields = ["usuario"]


@admin.register(TrilhaCurso)
class TrilhaCursoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "usuario", "ativa", "data_criacao"]
    list_filter = ["ativa", "data_criacao"]
    search_fields = ["titulo", "descricao", "solicitacao_original"]
    ordering = ["-data_criacao"]
    raw_id_fields = ["usuario"]
    readonly_fields = ["data_criacao", "data_atualizacao"]
