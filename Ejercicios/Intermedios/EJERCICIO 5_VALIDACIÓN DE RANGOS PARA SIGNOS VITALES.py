# ==========================================================
# EJERCICIO 5: VALIDACIÓN DE RANGOS PARA SIGNOS VITALES
# Nivel: Intermedio
# Tema: Salud (monitoreo)
#
# OBJETIVO:
# Usar excepciones personalizadas y validación de rangos
# para garantizar datos correctos.
# ==========================================================


class RangoInvalidoError(Exception):
    """Se lanza cuando un valor esta fuera del rango esperado"""
    pass

def validar_rango(valor, minimo, maximo, mensaje_error):
    if not (minimo <= valor <= maximo):
        raise RangoInvalidoError(mensaje_error)

def pedir_signo_vital(nombre, minimo, maximo):
    while True:
        try:  
            valor = float(input(f"Ingresa {nombre} {minimo}-{maximo} "))
            validar_rango(valor, minimo, maximo, f"{nombre} debe estar entre {minimo} y {maximo}")
            return valor
        except ValueError:
            print("Error: Debes ingesas un número.")
        except RangoInvalidoError as e:
            print(f"Error: {e}")
            
            
print("--- REGISTRO DE SIGNOS VITALES ---")
temp = pedir_signo_vital("Temperatura cardiaca (°C)", 35.0, 42.0)
fc = pedir_signo_vital("Frecuencia cardiaca (lpm)", 40,200)
sist = pedir_signo_vital("Presion sistolica (mmHg)", 90, 240)
diast = pedir_signo_vital("Presion diastolica (mmHg)", 60, 140)

print("\n--- DATOS REGISTRADOS ---")
print(f"Temperatura: {temp}°C")
print(f"Frecuencia cardiaca {fc} lpm")
print(f"Presion: {sist}/{diast} mmHg")