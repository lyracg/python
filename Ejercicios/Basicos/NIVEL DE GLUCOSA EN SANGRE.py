# ==========================================================
# EJERCICIO 15: NIVEL DE GLUCOSA EN SANGRE
# Nivel: Básico
# Tema: Salud (diabetes)
# ==========================================================

glucosa = float(input("Nivel de glucosa en ayunas (mg/dL): "))

if glucosa < 100:
    print("Nivel normal")
elif glucosa <= 125:
    print("Pediabetes, consulta a tu medico")    
else:
    print("Diabetes, necesitas atencion")