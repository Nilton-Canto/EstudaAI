# URLs do app usuarios
from django.urls import path
from . import views

# Configuração das rotas do app
urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Página de cadastro
    path('login/', views.login_view, name='login'),  # Página de login
]
