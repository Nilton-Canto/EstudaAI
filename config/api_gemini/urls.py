from django.urls import path
from . import views

app_name = 'api_gemini'

urlpatterns = [
    path('chat/', views.chat_with_gemini, name='chat_with_gemini'),
    path('health/', views.health_check, name='health_check'),
]
