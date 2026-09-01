# ==========================================================
# EJERCICIO 9: TABLA DE IMC PARA VARIOS PESOS
# Nivel: Básico
# Tema: Salud (nutrición)
# ==========================================================

altura = float(input("Altura en metros: "))

for i in range(1, 6):
    peso = float(input(f"Peso de la persona {i}: "))
    imc = peso / (altura **2)
    print(f"Persona {i}: IMC = {imc:.1f}")