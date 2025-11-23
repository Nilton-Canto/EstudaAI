from django.urls import path

from . import views

app_name = "api_gemini"

urlpatterns = [
    path("", views.test_api_page, name="test_api_page"),  # Página de teste
    path("chat/", views.chat_with_gemini, name="chat_with_gemini"),
    path("health/", views.health_check, name="health_check"),
    path("trilha/", views.gerar_trilha_curso, name="gerar_trilha_curso"),
    path(
        "trilhas/<int:user_id>/",
        views.listar_trilhas_usuario,
        name="listar_trilhas_usuario",
    ),
]
