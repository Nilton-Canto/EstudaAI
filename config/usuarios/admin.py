from django.contrib import admin  # importa o módulo de administração do Django.
from django.contrib.auth.admin import (  # importa a classe UserAdmin, que já traz toda a configuração padrão da interface de administração do Django para o modelo User.
    UserAdmin,
)

from .models import (  # mporta o modelo customizado de usuário (Usuario) definido em models.py.
    Usuario,
)


@admin.register(Usuario)  # registra o modelo Usuario no admin do Django.
class UsuarioAdmin(
    UserAdmin
):  # cria uma classe personalizada para controlar como o modelo Usuario será exibido no admin. Ela herda de UserAdmin.
    fieldsets = UserAdmin.fieldsets + (
        (
            "Informações acadêmicas",
            {"fields": ("nome", "universidade", "curso", "ano_formatura", "idade")},
        ),
    )  # pega os fieldsets originais do UserAdmin e adiciona um novo grupo chamado "Informações acadêmicas" com os campos extras criados.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("nome", "universidade", "curso", "ano_formatura", "idade")}),
    )  # Acrescenta também os campos extras (nome, universidade, curso, ano_formatura, idade) quando for cadastrar um novo usuário pela interface de admin.
    list_display = ("username", "email", "nome", "universidade", "curso")


# Esse arquivo serve para cadastro e exibição de usuários pelos admins do software
