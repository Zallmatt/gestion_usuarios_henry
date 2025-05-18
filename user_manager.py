from utils import validate_email, get_non_empty_input

def register_user():
    print("\n--- Registro de usuario ---")
    name = get_non_empty_input("Nombre: ")
    email = get_non_empty_input("Email: ", validate_email)
    password = get_non_empty_input("Contraseña: ")
    return {"name": name, "email": email, "password": password}

def list_users(users):
    print("\n--- Lista de usuarios ---")
    for idx, user in enumerate(users, 1):
        print(f"{idx}. {user['name']} - {user['email']}")

def search_user(users):
    name = input("Nombre a buscar: ").lower()
    found = [u for u in users if name in u["name"].lower()]
    if found:
        for user in found:
            print(f"Encontrado: {user['name']} - {user['email']}")
    else:
        print("No se encontró el usuario.")

def delete_user(users):
    email = input("Email del usuario a eliminar: ").lower()
    updated_users = [u for u in users if u["email"].lower() != email]
    if len(updated_users) < len(users):
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")
    return updated_users
