"""
Validadores customizados para a aplicação API.
"""

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validar_cor_hexadecimal(valor):
    """
    Valida se o valor é uma cor hexadecimal válida.

    Args:
        valor: String da cor (ex: #FF0000)

    Raises:
        ValidationError: Se a cor não for válida
    """
    if not valor.startswith("#") or len(valor) != 7:
        raise ValidationError(
            _("%(valor)s não é uma cor hexadecimal válida. Use o formato #RRGGBB"),
            params={"valor": valor},
        )

    try:
        int(valor[1:], 16)
    except ValueError:
        raise ValidationError(
            _("%(valor)s contém caracteres inválidos para uma cor hexadecimal."),
            params={"valor": valor},
        )


def validar_conteudo_json(valor):
    """
    Valida se o conteúdo é um JSON válido.

    Args:
        valor: String JSON

    Raises:
        ValidationError: Se o JSON não for válido
    """
    import json

    try:
        json.loads(valor)
    except json.JSONDecodeError as e:
        raise ValidationError(
            _("Conteúdo JSON inválido: %(error)s"),
            params={"error": str(e)},
        )
