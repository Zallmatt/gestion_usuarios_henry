from user_manager import register_user, list_users, search_user, delete_user
from file_manager import load_users, save_users
from dotenv import load_dotenv
from colorama import init, Fore, Style
import os

# Inicializar colorama
init(autoreset=True)

# Cargar variables de entorno
load_dotenv()
DATA_FILE = os.getenv("DATA_FILE", "users.json")

def main_menu():
    users = load_users(DATA_FILE)
    
    while True:
        print(Fore.CYAN + Style.BRIGHT + "="*40)
        print("        SISTEMA DE GESTIÓN DE USUARIOS        ")
        print("="*40 + Style.RESET_ALL)

        print(Fore.YELLOW + "📋 Menú principal")
        print("1️⃣  Registrar usuario")
        print("2️⃣  Listar usuarios")
        print("3️⃣  Buscar usuario")
        print("4️⃣  Eliminar usuario")
        print("5️⃣  Salir" + Style.RESET_ALL)

        option = input(Fore.GREEN + "\nElegí una opción: " + Style.RESET_ALL)

        print(Fore.BLUE + "-" * 40 + Style.RESET_ALL)

        if option == "1":
            user = register_user()
            users.append(user)
            save_users(users, DATA_FILE)
            print(Fore.GREEN + "✔ Usuario registrado correctamente.")
        elif option == "2":
            list_users(users)
        elif option == "3":
            search_user(users)
        elif option == "4":
            users = delete_user(users)
            save_users(users, DATA_FILE)
        elif option == "5":
            print(Fore.MAGENTA + "👋 ¡Gracias por usar el sistema!")
            break
        else:
            print(Fore.RED + "❌ Opción inválida.")
        
        input(Fore.LIGHTBLACK_EX + "\nPresioná ENTER para volver al menú..." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()
