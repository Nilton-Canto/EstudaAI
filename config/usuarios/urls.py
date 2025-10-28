# URLs do app usuarios
from django.urls import path
from . import views

# Configuração das rotas do app
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # Página inicial pós-login
    path('login/', views.login_view, name='login'),  # Página de login
    path('signup/', views.signup, name='signup'),  # Página de cadastro
]
