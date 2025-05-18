import json
import os

def load_users(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Archivo JSON vacío o corrupto. Inicializando lista vacía.")
            return []
    return []

def save_users(users, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)
