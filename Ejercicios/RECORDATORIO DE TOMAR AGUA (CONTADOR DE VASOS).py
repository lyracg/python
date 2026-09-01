# ==========================================================
# EJERCICIO 6: RECORDATORIO DE TOMAR AGUA
# Tema: Salud (hidratación)
#
# ==========================================================

vasos = 0

meta = 8

while vasos < meta:
    tomar = int(input("¿cuantos vasos de agua acabas de tomar ?: "))
    vasos = vasos + tomar
    print(f"llevas {vasos} vasos de agua de {meta}")    

print("Felicidades , has alcanzdo tu meta")    