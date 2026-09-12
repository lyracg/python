# ==========================================================
# EJERCICIO 8: USO DE TUPLAS PARA ALMACENAR SIGNOS VITALES
# Nivel: Intermedio
# Tema: Salud (monitoreo)
#
# OBJETIVO:
# Usar tuplas (inmutables) para representar un conjunto fijo de datos.
# ==========================================================

def crear_registro(temp, fc, sist, diast):
    return (temp, fc, sist, diast)

def mostrar_registro(registro):
    temp, fc, sist, diast = registro
    print(f"Temperatura: {temp}°C, FC: {fc} lpm, Presion: {sist}/{diast} mmHg")
    
r1 = crear_registro(36.3, 72, 120, 80)
mostrar_registro(r1)    


