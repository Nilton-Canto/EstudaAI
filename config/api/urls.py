from django.urls import path

from .views import AreaListView, TrilhaDetailView, TrilhaListCreateView
from .views_gemini import (
    chat_com_gemini,
    deletar_trilha_curso,
    detalhe_trilha_curso,
    gerar_trilha_curso,
    health_check,
    listar_trilhas_usuario,
    test_api_page,
)

urlpatterns = [
    # Endpoints de Áreas e Trilhas
    path("areas/", AreaListView.as_view(), name="lista-areas"),
    path("trilhas/", TrilhaListCreateView.as_view(), name="lista-trilhas"),
    path("trilhas/<int:pk>/", TrilhaDetailView.as_view(), name="detalhe-trilha"),
    # Endpoints Gemini AI
    path("gemini/gerar-trilha/", gerar_trilha_curso, name="gerar-trilha-curso"),
    path("gemini/trilha/", gerar_trilha_curso, name="gerar-trilha-curso-alias"),  # Alias para compatibilidade
    path("gemini/chat/", chat_com_gemini, name="chat-gemini"),
    path(
        "gemini/trilhas/", listar_trilhas_usuario, name="listar-trilhas-curso"
    ),
    path(
        "gemini/trilhas/<int:trilha_id>/",
        detalhe_trilha_curso,
        name="detalhe-trilha-curso",
    ),
    path(
        "gemini/trilhas/<int:trilha_id>/deletar/",
        deletar_trilha_curso,
        name="deletar-trilha-curso",
    ),
    path("gemini/health/", health_check, name="gemini-health"),
    path("gemini/test/", test_api_page, name="test-gemini"),
]
