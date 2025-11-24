"""
Exceções customizadas para a aplicação API.
"""

from rest_framework.exceptions import APIException


class TrilhaLimitExceededException(APIException):
    """Exceção lançada quando o usuário excede o limite de trilhas."""

    status_code = 400
    default_detail = "Você atingiu o limite máximo de trilhas permitidas."
    default_code = "trilha_limit_exceeded"


class AreaInativaException(APIException):
    """Exceção lançada quando tenta criar trilha em área inativa."""

    status_code = 400
    default_detail = "Não é possível criar trilha em uma área inativa."
    default_code = "area_inativa"


class TrilhaNaoEncontradaException(APIException):
    """Exceção lançada quando a trilha não é encontrada."""

    status_code = 404
    default_detail = "Trilha não encontrada."
    default_code = "trilha_not_found"


class GeminiAPIException(APIException):
    """Exceção lançada quando há erro na API do Gemini."""

    status_code = 500
    default_detail = "Erro ao comunicar com a API do Gemini."
    default_code = "gemini_api_error"


class InvalidJSONResponseException(APIException):
    """Exceção lançada quando a resposta do Gemini não é JSON válido."""

    status_code = 500
    default_detail = "Resposta da IA não está em formato válido."
    default_code = "invalid_json_response"
