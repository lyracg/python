# ==========================================================
# EJERCICIO 2: CALCULADORA DE IMC CON VALIDACIÓN
# Nivel: Intermedio
# Tema: Salud (nutrición)
#
# OBJETIVO:
# Aprender a usar try/except para manejar errores de entrada,
# definir funciones con retorno y usar la estructura if-elif-else.
# ==========================================================

def solicitar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("El valos debe ser mayor que cero, intente de nuevo")
                continue
            return valor
        except ValueError:
            print("Error: Debes ingresar un numero valido, usa puntos decimales")
            

def calcular_imc(peso, altura):
    return peso /(altura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo Peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    print("=== CALCULADORA DE IMC ===")
    peso = solicitar_numero("Ingresa tu peso en kg: ")
    altura = solicitar_numero("Ingresa tu altura en metros: ")           
    imc = calcular_imc(peso, altura)
    categoria = clasificar_imc(imc)
    print(f"Tu IMC es: {imc:.2f}")
    print(f"Clasificacion {categoria}")
    

if __name__ == "__main__":
    main()    