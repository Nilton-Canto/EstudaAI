# URLs principais do projeto
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from usuarios import views as usuarios_views

# Configuração das rotas principais
urlpatterns = [
    path("", usuarios_views.home, name="home"),  # Landing page na raiz
    path("login/", usuarios_views.login_view, name="login"),  # Login
    path("signup/", usuarios_views.signup, name="signup"),  # Cadastro
    path("logout/", usuarios_views.logout_view, name="logout"),  # Logout
    path("admin/", admin.site.urls),
    path(
        "usuarios/", include("usuarios.urls")
    ),  # URLs do app usuarios (dashboard, admin, etc.)
    path("api/", include("api.urls")),  # URLs da API (incluindo Gemini)
]

# Serve arquivos estáticos durante desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
