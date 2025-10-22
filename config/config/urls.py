from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # URLs do app usuarios (signup, login, etc.)
    path('api/gemini/', include('api_gemini.urls')),  # URLs da API do Gemini
]
