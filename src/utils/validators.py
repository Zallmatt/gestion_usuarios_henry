import re

# ✅ Funciones de validación lógica (testables)
def is_valid_name(name):
    return (
        name and
        all(c.isalpha() or c.isspace() for c in name) and
        len(name) >= 2
    )

def is_valid_password(password):
    return (
        password and
        len(password) >= 8 and
        any(c.isdigit() for c in password) and
        any(c.isalpha() for c in password)
    )

def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# ✅ Funciones interactivas (para uso en consola)
def name_validation():
    while True:
        name = input("Nombre: ").strip()
        if not is_valid_name(name):
            print("❌ Nombre inválido. Solo letras, espacios y mínimo 2 caracteres.")
            continue
        return name

def password_validation():
    while True:
        password = input("Contraseña: ").strip()
        if not is_valid_password(password):
            print("❌ La contraseña debe tener al menos 8 caracteres, una letra y un número.")
            continue
        return password

def validate_email():
    while True:
        email = input("Email: ").strip()
        if not is_valid_email(email):
            print("❌ Email inválido. Debe contener '@' y un dominio.")
            continue
        return email
