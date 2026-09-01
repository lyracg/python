# ==========================================================
# EJERCICIO 4: CALCULADORA DE CALORÍAS QUEMADAS AL CAMINAR
# Tema: Salud (ejercicio)
#
# OBJETIVO:
# Hacer operaciones matemáticas con variables y mostrar el resultado.
# ==========================================================

# Solcitamos el peso en kilogramas
peso = float(input("¿Cuanto pesas en kg ?: "))

# solicitamos los minutos que camina 
minutos = float(input("¿Cuantos minutos caminaste hoy ?: "))

calorias = peso * minutos * 0.03

print(f"Quemaste aporximadamente {calorias:.1f} calorias.")