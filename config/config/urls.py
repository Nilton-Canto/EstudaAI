# URLs principais do projeto
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from usuarios import views

# Configuração das rotas principais
urlpatterns = [
    path(
        "", lambda request: redirect("usuarios/login/")
    ),  # Redireciona raiz para login
    path("admin/", admin.site.urls),
    path(
        "usuarios/", include("usuarios.urls")
    ),  # URLs do app usuarios (signup, login, etc.)
    path("api/", include("api.urls")),  # URLs da API (incluindo Gemini)
]

# Serve arquivos estáticos durante desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
