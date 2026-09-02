# ==========================================================
# EJERCICIO 13: TEMPORIZADOR PARA TOMAR MEDICAMENTO (SIMULACIÓN)
# Nivel: Básico
# Tema: Salud (medicación)
# ==========================================================

import time

intervalo_horas = float(input("Cada cuantas horas debes tomar el medicamento?: "))
dosis_totales = int(input("Numero total de dosis: "))

for dosis in range(1, dosis_totales + 1):
    tiempo_espera = intervalo_horas * 3600
    print(f"Esperando {intervalo_horas} hora(s) para la dosis {dosis} . . .")
    time.sleep(tiempo_espera)
    print(f"Hoa de tomar la dosis {dosis}")

print("Tratamiento completado")    