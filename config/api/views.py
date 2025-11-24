from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Area, Trilha
from .serializers import AreaSerializer, TrilhaSerializer

# =============================
#   ÁREAS
# =============================


class AreaListView(generics.ListAPIView):
    queryset = Area.objects.filter(ativa=True)
    serializer_class = AreaSerializer
    permission_classes = [permissions.AllowAny]


# =============================
#   TRILHAS DO ESTUDANTE
# =============================


class TrilhaListCreateView(generics.ListCreateAPIView):
    serializer_class = TrilhaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trilha.objects.filter(usuario=self.request.user, ativa=True)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class TrilhaDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrilhaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trilha.objects.filter(usuario=self.request.user)
