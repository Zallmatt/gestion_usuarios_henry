import re

def get_non_empty_input(prompt, validation_func=None):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Este campo no puede estar vacío.")
            continue
        if validation_func and not validation_func(value):
            print("Valor inválido.")
            continue
        return value

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
