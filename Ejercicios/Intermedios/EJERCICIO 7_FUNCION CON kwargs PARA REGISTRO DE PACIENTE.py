# ==========================================================
# EJERCICIO 10: FUNCIÓN CON **kwargs PARA REGISTRO DE PACIENTE
# Nivel: Intermedio
# Tema: Salud (administración)
#
# OBJETIVO:
# Usar **kwargs para aceptar un número variable de argumentos
# con nombre (clave=valor) y crear un diccionario de paciente.
# ==========================================================

def registrar_paciente(**kwargs):
    paciente = dict(kwargs)
    if 'id' not in paciente:
        import time
        paciente['id'] = int(time.time()) % 10000
    return paciente


def mostrar_paciente(paciente):
    print("\n--- DATOS DEL PACIENTE ---")
    for clave, valor in paciente.items():
        print(f"{clave}: {valor}")

        
    
print("--- REGISTRO DE PACIENTE ---")
paciente1 = registrar_paciente(
    nombre = "Ana Garcia",
    edad = 45,
    diagnostico = "Hipertension",
    telefono = "555-1234"
)

mostrar_paciente(paciente1)

paciente2= registrar_paciente(
    nombre = "Carlos Ortiz",
    edad = 72,
    diagnostico = "Diabetes tipo 2"
)

mostrar_paciente(paciente2)

paciente3 = registrar_paciente(
    nombre = "Karina Ortega",
    edad = 30,
    diagnostico = "Sana",
    alergias = "Ninguna",
    grupo_sanguineo = "O+"
)

mostrar_paciente(paciente3)