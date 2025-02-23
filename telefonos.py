import re

def validar_telefono(numero):
    patron = r'^\+\d{2}-\d{3}-\d{3}-\d{4}$'
    return bool(re.match(patron, numero))

# Pruebas con assert
def test_validar_telefono():
    assert validar_telefono("+12-345-678-9012") == True  # Válido
    assert validar_telefono("12-345-678-9012") == False  # Falta el "+"
    assert validar_telefono("+123-456-789-0123") == False  # Prefijo de país incorrecto (debe ser 2 dígitos)
    assert validar_telefono("+12-3456-789-012") == False  # Error en los bloques de números

# Ejecutar pruebas
test_validar_telefono()
print(" las pruebas pasaron")
