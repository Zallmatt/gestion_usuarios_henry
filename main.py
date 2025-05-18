from user_manager import register_user, list_users, search_user, delete_user
from file_manager import load_users, save_users
import os
from dotenv import load_dotenv

load_dotenv()
DATA_FILE = os.getenv("DATA_FILE", "users.json")

users = load_users(DATA_FILE)

def main_menu():
    
    users = load_users(DATA_FILE)
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        option = input("Elegí una opción: ")

        if option == "1":
            user = register_user()
            users.append(user)
            save_users(users, DATA_FILE)
        elif option == "2":
            list_users(users)
        elif option == "3":
            search_user(users)
        elif option == "4":
            users = delete_user(users)
            save_users(users, DATA_FILE)
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main_menu()
