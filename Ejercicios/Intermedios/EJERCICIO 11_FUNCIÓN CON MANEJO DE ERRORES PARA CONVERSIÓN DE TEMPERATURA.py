# ==========================================================
# EJERCICIO 11: FUNCIÓN CON MANEJO DE ERRORES PARA CONVERSIÓN DE TEMPERATURA
# Nivel: Intermedio
# Tema: Salud (monitoreo)
#
# OBJETIVO:
# Usar try/except para validar que el usuario ingrese números válidos.
# ==========================================================

def convertir_fahrenheit_a_celsius():
    while True:
        try:
            f = float(input("Ingresa la temperatura en °F: "))
            c = ((f - 32) * 5) / 9
            return c 
        except ValueError:
            print("Error : Debesa ingresar un numero valido, intenta de nuevo: ")
            
            
temp_c = convertir_fahrenheit_a_celsius()
print(f"Temperatura en Celsius: {temp_c:.1f}°C ")            

