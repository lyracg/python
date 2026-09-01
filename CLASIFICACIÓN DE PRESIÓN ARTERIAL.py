# ==========================================================
# EJERCICIO 3: CLASIFICACIÓN DE PRESIÓN ARTERIAL
# Nivel: Básico
# Tema: Salud (cardiología)
#
# OBJETIVO:
# Usar condiciones múltiples con operadores lógicos (and, or) para
# clasificar la presión arterial según las guías médicas.
# ==========================================================

sistolica = int(input("Presión sistolica (numero alto: "))
distolica = int(input("Presion diastolica (numero mas bajo: )"))

if sistolica < 120 and distolica < 80:
    print("Presión normal")
elif sistolica < 130 and distolica < 80:
    print("Presion elevada")
elif (sistolica >= 130 and sistolica <= 139) or (distolica >= 80 and distolica <= 89):
    print("Hipertension etapa 1")
else:
    print("Hipertencio etapa 2")    