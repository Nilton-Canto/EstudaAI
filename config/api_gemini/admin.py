from django.contrib import admin

from .models import TrilhaCurso


@admin.register(TrilhaCurso)
class TrilhaCursoAdmin(admin.ModelAdmin):
    """Configuração do admin para TrilhaCurso"""

    list_display = ("titulo", "usuario", "data_criacao", "ativa")
    list_filter = ("ativa", "data_criacao", "data_atualizacao")
    search_fields = ("titulo", "descricao", "usuario__username", "usuario__nome")
    readonly_fields = ("data_criacao", "data_atualizacao")

    fieldsets = (
        (
            "Informações Básicas",
            {"fields": ("usuario", "titulo", "descricao", "ativa")},
        ),
        (
            "Conteúdo",
            {
                "fields": ("solicitacao_original", "conteudo_json"),
                "classes": ("collapse",),
            },
        ),
        (
            "Timestamps",
            {"fields": ("data_criacao", "data_atualizacao"), "classes": ("collapse",)},
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        """Campos readonly baseados no contexto"""
        readonly = list(self.readonly_fields)
        if obj:  # editing an existing object
            readonly.extend(["usuario"])
        return readonly
