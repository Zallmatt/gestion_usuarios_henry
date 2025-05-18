# 📘 Sistema de Gestión de Usuarios en Python

Este proyecto es una práctica de programación en Python que simula un sistema básico de gestión de usuarios a través de la consola. Permite registrar, listar, buscar, eliminar y guardar usuarios usando archivos externos para persistencia.

---

## 🚀 Funcionalidades

- Registrar nuevos usuarios (nombre, email, contraseña)
- Listar todos los usuarios registrados
- Buscar usuarios por nombre
- Eliminar usuarios por email
- Guardar y cargar los usuarios desde un archivo JSON
- Interfaz interactiva por consola
- Modularización del código en distintos archivos

---

## 🧪 Tecnologías usadas

- Python 3.10+
- Librería `python-dotenv` para variables de entorno
- Entorno virtual (`venv`)
- Formato de datos: JSON

---

## 🗂️ Estructura del proyecto
├── main.py # Menú principal
├── user_manager.py # Lógica de usuarios
├── file_manager.py # Guardado y carga de datos
├── utils.py # Validaciones y funciones auxiliares
├── users.json # Archivo con usuarios registrados
├── .env # Variables de entorno
├── requirements.txt # Dependencias del proyecto
├── .gitignore
└── README.md

---

## ⚙️ Instalación y uso

1. **Clonar el repositorio**
```bash
git clone https://github.com/Zallmatt/gestion_usuarios_henry.git

2. **Crear y activar el entorno virtual**

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
#Instalar dependencias
pip install -r requirements.txt
#Ejecutar el programa
python main.py


