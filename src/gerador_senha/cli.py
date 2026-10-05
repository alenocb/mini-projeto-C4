"""Interface de linha de comando do gerador de senhas."""

import click

from gerador_senha.generator import generate_password


@click.command()
@click.option("--length", "-l", default=16, type=click.IntRange(1, 256), show_default=True)
@click.option("--lowercase/--no-lowercase", default=True, help="Incluir letras minusculas.")
@click.option("--uppercase/--no-uppercase", default=True, help="Incluir letras maiusculas.")
@click.option("--digits/--no-digits", default=True, help="Incluir numeros.")
@click.option(
    "--special-characters/--no-special-characters",
    default=False,
    help="Incluir caracteres especiais.",
)
def main(
    length: int,
    lowercase: bool,
    uppercase: bool,
    digits: bool,
    special_characters: bool,
) -> None:
    """Gera uma senha aleatoria conforme os grupos escolhidos."""
    try:
        password = generate_password(
            length,
            lowercase=lowercase,
            uppercase=uppercase,
            digits=digits,
            special_characters=special_characters,
        )
    except ValueError as error:
        raise click.UsageError(str(error)) from error

    click.echo(password)