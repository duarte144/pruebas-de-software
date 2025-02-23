

def calcular_puntuacion(puntos, bonus):
    if puntos >= 100 and bonus:
        return "Oro"
    elif puntos >= 50 and puntos < 100:
        return "Plata"
    else:
        return "Bronce"
    
    

# Función de pruebas con assert
def test_calcular_puntuacion():
    assert calcular_puntuacion(120, True) == "Oro"    # Caso de oro
    assert calcular_puntuacion(120, False) == "Bronce"  # Sin bonus no es oro
    assert calcular_puntuacion(80, True) == "Plata"   #  rango de plata
    assert calcular_puntuacion(30, True) == "Bronce"  # Menos de 50, bronce
    assert calcular_puntuacion(100, True) == "Oro"    # Justo en 100 con bonus
    assert calcular_puntuacion(100, False) == "Bronce" # 100 sin bonus
    assert calcular_puntuacion(50, True) == "Plata"   # Límite inferior de plata
    assert calcular_puntuacion(49, False) == "Bronce" #  debajo de plata

    print(" las pruebas pasaron")

# Ejecutar pruebas
test_calcular_puntuacion()

