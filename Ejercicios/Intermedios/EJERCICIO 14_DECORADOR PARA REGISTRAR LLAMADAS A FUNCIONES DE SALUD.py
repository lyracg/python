# ==========================================================
# EJERCICIO 14: DECORADOR PARA REGISTRAR LLAMADAS A FUNCIONES DE SALUD
# Nivel: Intermedio
# Tema: Salud (bitácora)
#
# OBJETIVO:
# Crear un decorador que imprima un mensaje antes y después de ejecutar una función.
# ==========================================================

def registrar_llamdas(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} devolvio {resultado}")
        return resultado
    return wrapper

@registrar_llamdas
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

imc = calcular_imc(70, 1.75)
print(f"IMC = {imc:.1f}")

