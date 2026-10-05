"""Funcoes para gerar senhas aleatorias com fontes criptograficas."""

import secrets
import string


def generate_password(
    length: int = 16,
    *,
    lowercase: bool = True,
    uppercase: bool = True,
    digits: bool = True,
    special_characters: bool = False,
) -> str:
    """Gera uma senha e garante ao menos um caractere de cada grupo ativo."""
    groups = []
    if lowercase:
        groups.append(string.ascii_lowercase)
    if uppercase:
        groups.append(string.ascii_uppercase)
    if digits:
        groups.append(string.digits)
    if special_characters:
        groups.append(string.punctuation)

    if not groups:
        raise ValueError("Ative ao menos um grupo de caracteres.")
    if length < len(groups):
        raise ValueError(
            f"O tamanho precisa ser de pelo menos {len(groups)} para incluir "
            "todos os grupos selecionados."
        )

    alphabet = "".join(groups)
    password = [secrets.choice(group) for group in groups]
    password.extend(secrets.choice(alphabet) for _ in range(length - len(password)))
    secrets.SystemRandom().shuffle(password)
    return "".join(password)