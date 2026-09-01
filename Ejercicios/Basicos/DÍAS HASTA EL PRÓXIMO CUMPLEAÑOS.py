# ==========================================================
# EJERCICIO 5: DÍAS HASTA EL PRÓXIMO CUMPLEAÑOS
# Tema: Salud (prevención)
#
# OBJETIVO:
# Usar el módulo datetime para manejar fechas y calcular la diferencia en días.
# ==========================================================

from datetime import datetime

dia = int(input("¿Que día naciste ? "))

mes = int(input("¿Que mes naciste ? "))

hoy = datetime.now()

proximo_cumple = datetime(hoy.year, mes, dia)

if proximo_cumple < hoy:
    proximo_cumple = proximo_cumple.replace(year = hoy.year + 1)

dias_faltan = (proximo_cumple - hoy).days

print(f"Faltan {dias_faltan} días para tu proximo cumpleaños.")
