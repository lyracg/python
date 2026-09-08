# ==========================================================
# EJERCICIO 6: FUNCIÓN CON *args PARA PROMEDIO DE VARIAS MEDICIONES
# Nivel: Intermedio
# Tema: Salud (monitoreo)
#
# OBJETIVO:
# Usar *args para permitir que una función reciba un número variable
# de argumentos y calcular el promedio de todos ellos.
# ==========================================================

def promedio_mediciones(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

def estadisticas_mediciones(*args):
    if not args:
        return (0, None, None, 0)
    return (sum(args) / len(args), max(args), min(args), len(args))

print("--- ÁNALISIS DE MEDICIONES ---")
mediciones = []
while True:
    valor = input("Ingresa una medición (0 'fin' para terminar): ")
    if valor.lower() == 'fin':
        break
    try:
        mediciones.append(float(valor))
    except ValueError:
        print("Valor no válido. Ingresa un número.")
        
prom = promedio_mediciones(*mediciones)
prom, maximo, minimo, cantidad = estadisticas_mediciones(*mediciones)

print(f"\nCantidad de mediciones: {cantidad}")
print(f"Promedio: {prom:.2f}")
if maximo is not None:
    print(f"Maximo: {maximo}")
    print(f"Minimo: {minimo}")

