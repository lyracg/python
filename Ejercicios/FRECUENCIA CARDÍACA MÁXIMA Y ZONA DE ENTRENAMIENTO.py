# ==========================================================
# EJERCICIO 7: FRECUENCIA CARDÍACA MÁXIMA Y ZONA DE ENTRENAMIENTO
# Nivel: Básico
# Tema: Salud (ejercicio)
# ==========================================================

edad = int(input("¿Cuantos años tienes ? "))

frec_max = 220 - edad

zona_baja = frec_max * 0.50
zona_alta = frec_max * 0.85

print(f"Tu frecuencia cardiaca maxima es: {frec_max} latidos por miuto")
print(f"Para un entrenamiento cardiovascular, tu frecuencia debe estare entre: ")
print(f"{int(zona_baja)} y {int(zona_alta)} latidos por minuto")