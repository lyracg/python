# ==========================================================
# EJERCICIO 10: FUNCIÓN PARA CALCULAR IMC
# Nivel: Básico
# Tema: Salud (nutrición)
# ==========================================================

def calcular_imc(peso, altura):
    resultado = peso / (altura ** 2)
    return resultado

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = calcular_imc(peso, altura)

print(f"Tu IMC es {imc:.1f}")