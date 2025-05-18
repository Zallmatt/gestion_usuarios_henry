from utils.validators import validate_email, name_validation, password_validation
from colorama import Fore, Style

def register_user():
    print("\n--- Registro de usuario ---")
    name = name_validation()
    email = validate_email()
    password = password_validation()
    return {"name": name, "email": email, "password": password}

def list_users(users):
    print(Fore.YELLOW + "\n📋 Lista de usuarios:\n" + Style.RESET_ALL)
    for idx, user in enumerate(users, 1):
        #Recorremos la lista 'users' y enumeramos cada usuario con idx arrancando desde 1
        print(Fore.WHITE + f"{idx}. {user['name']} - {user['email']}")

def search_user(users):
    name = input(Fore.WHITE + "🔎 Nombre a buscar: ").lower()
    # Se crea una lista 'found' con los usuarios cuyo nombre contiene el texto buscado
    found = [u for u in users if name in u["name"].lower()]
    if found:
        for user in found:
            print(Fore.GREEN + f"✅ Encontrado: {user['name']} - {user['email']}")
    else:
        print(Fore.RED + "❌ No se encontró el usuario.")

def delete_user(users):
    email = input("✉️  Email del usuario a eliminar: ").lower()
    updated_users = [u for u in users if u["email"].lower() != email]
    if len(updated_users) < len(users):
        print(Fore.GREEN + "🗑️ Usuario eliminado.")
    else:
        print(Fore.RED + "❌ Usuario no encontrado.")
    return updated_users
