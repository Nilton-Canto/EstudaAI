from django.urls import path
from .views import AreaListView, TrilhaListCreateView, TrilhaDetailView

urlpatterns = [
    path("areas/", AreaListView.as_view(), name="lista-areas"),
    path("trilhas/", TrilhaListCreateView.as_view(), name="lista-trilhas"),
    path("trilhas/<int:pk>/", TrilhaDetailView.as_view(), name="detalhe-trilha"),
]
