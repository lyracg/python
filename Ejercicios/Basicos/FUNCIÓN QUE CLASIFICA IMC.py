# ==========================================================
# EJERCICIO 11: FUNCIÓN QUE CLASIFICA IMC
# Nivel: Básico
# Tema: Salud (nutrición)
# ==========================================================

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
    
peso = float(input("Peso: ")) 
altura = float(input("Altura: "))
imc_valor = calcular_imc(peso, altura)
categoria = clasificar_imc(imc_valor)

print(f"IMC: {imc_valor:.1f} - {categoria}")
