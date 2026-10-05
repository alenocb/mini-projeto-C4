# Gerador de Senhas

CLI em Python para gerar senhas aleatorias com selecao de tamanho e grupos de caracteres. A geracao usa o modulo `secrets` da biblioteca padrao do Python.

## Requisitos

Python 3.10 ou superior.

## Instalar

Na raiz do projeto, instale o pacote em modo editavel:

```powershell
python -m pip install -e ".[test]"
```

## Usar

```powershell
python -m gerador_senha --length 20 --special-characters
python -m gerador_senha --length 24 --special-characters
python -m gerador_senha --length 32 --no-uppercase --no-digits
```

O tamanho padrao e 16. Letras minusculas, maiusculas e numeros sao incluidos por padrao; caracteres especiais sao opcionais. Para cada grupo ativado, a senha tera ao menos um caractere desse grupo. O tamanho deve comportar todos os grupos escolhidos. Com o ambiente Python ativado, o comando instalado `senha-segura` pode ser usado no lugar de `python -m gerador_senha`.

Para ver todas as opcoes:

```powershell
python -m gerador_senha --help
```

## Testes

```powershell
python -m pytest
```
