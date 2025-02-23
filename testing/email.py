import re


def validar_email(email):
    
    patron = r'[\w.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}'


    return bool(re.match(patron, email))

# Pruebas con assert
def test_validar_email():
    assert validar_email("juan.perez@empresa.com") == True  # Válido
    assert validar_email("maria@dominio") == False  # Inválido (falta extensión)
    assert validar_email("pedro#2024@mail.org") == False  # Inválido (# no permitido)

# Ejecutar pruebas
test_validar_email()
print("Todas las pruebas pasaron correctamente.")
