import string

import pytest
from click.testing import CliRunner

from gerador_senha.cli import main
from gerador_senha.generator import generate_password


def test_password_has_requested_length_and_each_selected_group():
    password = generate_password(
        4, lowercase=True, uppercase=True, digits=True, special_characters=True
    )

    assert len(password) == 4
    assert any(character in string.ascii_lowercase for character in password)
    assert any(character in string.ascii_uppercase for character in password)
    assert any(character in string.digits for character in password)
    assert any(character in string.punctuation for character in password)


def test_password_uses_only_selected_groups():
    password = generate_password(
        40, lowercase=False, uppercase=False, digits=True, special_characters=False
    )

    assert password.isdigit()


def test_rejects_when_no_group_is_selected():
    with pytest.raises(ValueError, match="ao menos um grupo"):
        generate_password(
            12, lowercase=False, uppercase=False, digits=False, special_characters=False
        )


def test_rejects_length_shorter_than_selected_groups():
    with pytest.raises(ValueError, match="pelo menos 2"):
        generate_password(
            1, lowercase=True, uppercase=True, digits=False, special_characters=False
        )


def test_cli_prints_password():
    result = CliRunner().invoke(main, ["--length", "20", "--special-characters"])

    assert result.exit_code == 0
    assert len(result.output.strip()) == 20
