# ==========================================================
# EJERCICIO 12: DETERMINACIÓN DE DONANTE DE SANGRE
# Nivel: Básico
# Tema: Salud (donación)
# ==========================================================

edad = int(input("Edad: "))
peso = float(input("Peso en Kg: "))

if (edad >= 18 and edad <= 65) and (peso > 50):
    print("Cumples con los requisitos")
else:
    if edad < 18 or edad > 65:
        print("No cumples con el rango de edad")
    if peso <= 50:
        print("Debes de pesar mas de 50 kg")