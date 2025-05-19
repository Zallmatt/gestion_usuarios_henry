import unittest
from utils.validators import is_valid_email, is_valid_password

'''
Para testear debe hacer
1- cd src
2- python -m tests.test_user_manager
'''

class TestUserManager(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(is_valid_email("ejemplo@correo.com"), "Email válido falló")
        self.assertTrue(is_valid_email("test123@dominio.org"), "Email con números falló")
        self.assertFalse(is_valid_email("correo_invalido"), "Email inválido sin dominio no falló")
        self.assertFalse(is_valid_email("otro@.com"), "Email inválido sin nombre no falló")
        self.assertFalse(is_valid_email(""), "Email vacío no falló")

    def test_password_rules(self):
        self.assertTrue(is_valid_password("abc12345"), "Contraseña válida falló")
        self.assertFalse(is_valid_password("abc12"), "Contraseña corta no falló")
        self.assertFalse(is_valid_password("abcdefgh"), "Contraseña sin número no falló")
        self.assertFalse(is_valid_password("12345678"), "Contraseña sin letras no falló")

    def test_search_user_found(self):
        users = [
            {"name": "Matias", "email": "matias@gmail.com", "password": "abc123"},
            {"name": "Lucia", "email": "lucia@gmail.com", "password": "def456"}
        ]
        search = "matias"
        found = [u for u in users if search in u["name"].lower()]
        self.assertEqual(len(found), 1, "Usuario 'matias' no fue encontrado")
        self.assertEqual(found[0]["email"], "matias@gmail.com", "Email de Matias incorrecto")

    def test_search_user_not_found(self):
        users = [{"name": "Ana", "email": "ana@gmail.com", "password": "abc123"}]
        search = "pedro"
        found = [u for u in users if search in u["name"].lower()]
        self.assertEqual(len(found), 0, "Se encontró un usuario que no existe")

if __name__ == "__main__":
    unittest.main()
