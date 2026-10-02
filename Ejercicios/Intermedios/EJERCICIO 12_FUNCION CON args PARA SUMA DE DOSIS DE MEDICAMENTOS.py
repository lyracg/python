# ==========================================================
# EJERCICIO 12: FUNCIÓN CON *args PARA SUMA DE DOSIS DE MEDICAMENTOS
# Nivel: Intermedio
# Tema: Salud (medicación)
#
# OBJETIVO:
# Usar *args para sumar un número variable de dosis (en mg).
# ==========================================================

def dosis_total(*args):
    total = 0
    for dosis in args:
        total += dosis
    return total

total = dosis_total(500, 200, 100)
print(f"Dosis total diaria: {total} mg")

print(f"Dosis total: {dosis_total(250, 250)} mg")

lista_dosis = [50, 100, 150, 200]
print(f"Suma de listas: {dosis_total(*lista_dosis)} mg")

