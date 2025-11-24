"""
Constantes utilizadas na aplicação API.
"""

# Status de trilhas
STATUS_CHOICES = [
    ("rascunho", "Rascunho"),
    ("publicada", "Publicada"),
    ("arquivada", "Arquivada"),
]

# Dificuldades
DIFICULDADE_CHOICES = [
    ("iniciante", "Iniciante"),
    ("intermediario", "Intermediário"),
    ("avancado", "Avançado"),
]

# Cores padrão para áreas
CORES_PADRAO = [
    "#4f46e5",  # Indigo
    "#f59e0b",  # Amber
    "#10b981",  # Emerald
    "#ef4444",  # Red
    "#8b5cf6",  # Violet
    "#ec4899",  # Pink
    "#06b6d4",  # Cyan
    "#f97316",  # Orange
]

# Limites
MAX_TRILHAS_POR_USUARIO = 50
MAX_AREAS_ATIVAS = 100
