# URLs principais do projeto
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios import views

# Configuração das rotas principais
urlpatterns = [
    path('admin/', admin.site.urls),  # Painel administrativo
    path('', include('usuarios.urls')),  # Inclui URLs do app usuarios
]

# Serve arquivos estáticos durante desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)