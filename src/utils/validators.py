import re

def name_validation():
    while True:
        name = input("Nombre: ").strip()
        if not name:
            print("❌ Este campo no puede estar vacío.")
            continue
        if not all(c.isalpha() or c.isspace() for c in name):
            print("❌ Nombre inválido. Solo se permiten letras y espacios.")
            continue
        if len(name) < 2:
            print("❌ El nombre debe tener al menos 2 caracteres.")
            continue
        return name

def password_validation():
    while True:
        password = input("Contraseña: ").strip()
        if not password:
            print("❌ Este campo no puede estar vacío.")
            continue
        if len(password) < 8:
            print("❌ La contraseña debe tener al menos 8 caracteres.")
            continue
        if not any(char.isdigit() for char in password):
            print("❌ La contraseña debe contener al menos un número.")
            continue
        if not any(char.isalpha() for char in password):
            print("❌ La contraseña debe contener al menos una letra.")
            continue
        return password

def validate_email():
    while True:
        email = input("Email: ").strip()
        if not email:
            print("❌ Este campo no puede estar vacío.")
            continue
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("❌ Email inválido. Debe contener '@' y un dominio.")
            continue
        return email
