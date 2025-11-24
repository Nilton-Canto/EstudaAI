# URLs do app usuarios
from django.urls import path

from . import views

# Configuração das rotas do app
urlpatterns = [
    # URLs públicas
    path("dashboard/", views.dashboard, name="dashboard"),  # Página inicial pós-login
    # URLs administrativas
    path(
        "admin-panel/", views.admin_dashboard, name="admin_dashboard"
    ),  # Dashboard admin
    # CRUD Usuários
    path(
        "admin-panel/usuarios/", views.admin_usuarios_list, name="admin_usuarios_list"
    ),
    path(
        "admin-panel/usuarios/criar/",
        views.admin_usuario_create,
        name="admin_usuario_create",
    ),
    path(
        "admin-panel/usuarios/<int:pk>/editar/",
        views.admin_usuario_edit,
        name="admin_usuario_edit",
    ),
    path(
        "admin-panel/usuarios/<int:pk>/excluir/",
        views.admin_usuario_delete,
        name="admin_usuario_delete",
    ),
    # CRUD Áreas
    path("admin-panel/areas/", views.admin_areas_list, name="admin_areas_list"),
    path("admin-panel/areas/criar/", views.admin_area_create, name="admin_area_create"),
    path(
        "admin-panel/areas/<int:pk>/editar/",
        views.admin_area_edit,
        name="admin_area_edit",
    ),
    path(
        "admin-panel/areas/<int:pk>/excluir/",
        views.admin_area_delete,
        name="admin_area_delete",
    ),
    # CRUD Trilhas
    path("admin-panel/trilhas/", views.admin_trilhas_list, name="admin_trilhas_list"),
    path(
        "admin-panel/trilhas/criar/",
        views.admin_trilha_create,
        name="admin_trilha_create",
    ),
    path(
        "admin-panel/trilhas/<int:pk>/editar/",
        views.admin_trilha_edit,
        name="admin_trilha_edit",
    ),
    path(
        "admin-panel/trilhas/<int:pk>/excluir/",
        views.admin_trilha_delete,
        name="admin_trilha_delete",
    ),
    # URLs de chat IA
    path("chat-ia/", views.chat_ia, name="chat_ia"),
    # URLs de trilhas do usuário
    path("minhastrilhas/", views.minhas_trilhas, name="minhas_trilhas"),
    path("criartrilha/", views.criar_trilha, name="criar_trilha"),
    path("trilha/<int:pk>/", views.ver_trilha, name="ver_trilha"),
    path("trilha/<int:pk>/excluir/", views.excluir_trilha, name="excluir_trilha"),
    path("trilha/<int:pk>/marcar/", views.marcar_atividade, name="marcar_atividade"),
    path("trilha/<int:pk>/marcar-modulo/", views.marcar_modulo, name="marcar_modulo"),
]
