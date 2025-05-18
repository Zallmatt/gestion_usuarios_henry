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

```
├── main.py             # Menú principal
├── user_manager.py     # Lógica de usuarios
├── file_manager.py     # Guardado y carga de datos
├── utils.py            # Validaciones y funciones auxiliares
├── users.json          # Archivo con usuarios registrados
├── .env                # Variables de entorno
├── requirements.txt    # Dependencias del proyecto
├── .gitignore
└── README.md
```

---

## ⚙️ Instalación y uso

1. **Clonar el repositorio**
```bash
git clone https://github.com/Zallmatt/gestion_usuarios_henry.git
cd gestion_usuarios_henry
```

2. **Crear el entorno virtual**
```bash
python -m venv venv
```

3. **Activar el entorno virtual**

- En Windows:
```bash
venv\Scripts\activate
```

- En macOS/Linux:
```bash
source venv/bin/activate
```

4. **Instalar las dependencias**
```bash
pip install -r requirements.txt
```

5. **Ejecutar la aplicación**
```bash
python main.py
```

---

## 🧪 Tests unitarios

El proyecto incluye pruebas unitarias para validar funciones clave del sistema:

- ✅ Validación de emails (`is_valid_email`)
- ✅ Validación de contraseñas (`is_valid_password`)
- ✅ Simulación de búsquedas de usuarios (`search_user`)

### ▶ Cómo ejecutar los tests

Con el entorno virtual activo, ejecutá en la terminal:

```bash
python test_user_manager.py

## 📩 Contacto

Desarrollado por [Matías Zalazar]  
📧 matizalazar2001@gmail.com  
🔗 [GitHub/Zallmatt](https://github.com/Zallmatt)
