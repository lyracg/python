# ==========================================================
# EJERCICIO 14: FUNCIÓN RECURSIVA PARA CONTAR DÍAS DE TRATAMIENTO (SIMULACIÓN)
# Nivel: Intermedio
# Tema: Salud (tratamientos)
#
# OBJETIVO:
# Usar recursividad para simular el conteo de días restantes de un tratamiento.
# ==========================================================

def contar_dias(dias_restantes):
    if dias_restantes == 0:
        print("TRATAMIENTO COMPETADO")
        return
    else:
        print(f"Dias restantes {dias_restantes}")
        contar_dias(dias_restantes - 1)

dias = int(input("Cuantos dias dura el tratmiento ? : "))
contar_dias(dias)



