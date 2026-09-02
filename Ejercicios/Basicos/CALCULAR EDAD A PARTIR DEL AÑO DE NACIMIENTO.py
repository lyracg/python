# ==========================================================
# EJERCICIO 14: CALCULAR EDAD A PARTIR DEL AÑO DE NACIMIENTO
# Nivel: Básico
# Tema: Salud (datos personales)
# ==========================================================

from datetime import datetime

año_actual = datetime.now().year
año_nac = int(input("¿En que año naciste?: "))
edad = año_actual - año_nac

cumplio = input("Ya cumpliste años este año (s/n): ")

if cumplio.lower() == 'n':
    edad = edad - 1
    
print(f"Tienes {edad} años.")    