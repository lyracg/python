# ==========================================================
# EJERCICIO 8: CONTADOR DE PASOS (META DIARIA)
# Nivel: Básico
# Tema: Salud (actividad física)
# ==========================================================

total_pasos = 0
meta = 10000

while total_pasos < meta:
    pasos = int(input("¿cuantos pasos has dado ahora ? : "))
    if pasos == 0:
        print("Has terminado tu registro.")
        break
    total_pasos = total_pasos + pasos
    print(f"Llevas {total_pasos} pasos")
    
if total_pasos >= meta:
    print("Meta superada")
else:
    print(f"Te faltaron {meta - total_pasos} pasos ")        