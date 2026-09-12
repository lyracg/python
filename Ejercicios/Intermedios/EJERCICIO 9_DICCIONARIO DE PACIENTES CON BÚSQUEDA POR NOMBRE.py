# ==========================================================
# EJERCICIO 9: DICCIONARIO DE PACIENTES CON BÚSQUEDA POR NOMBRE
# Nivel: Intermedio
# Tema: Salud (administración)
#
# OBJETIVO:
# Usar un diccionario donde la clave es el nombre del paciente y el valor es otro diccionario con sus datos.
# ==========================================================

pacientes = {}

def agregar_paciente(nombre, edad, diagnostico):
    if nombre in pacientes:
        print(f"El pacientes {nombre} ya existe. No se agrego")
    else:
        pacientes[nombre] = {"edad": edad, "diagnostico": diagnostico}
        print(f"Paciente {nombre} agregado.")

def buscar_paciente(nombre):
    return pacientes.get(nombre)

        
agregar_paciente("Carlos", 35, "DIabetes")
agregar_paciente("Luis", 28, "Hipertencion")
agregar_paciente("Luis", 30, "Asma")

datos = buscar_paciente("Carlos")
if datos:
    print(f"Carlos: Edad {datos['edad']}, Diagnostico: {datos['diagnostico']}")
else:
    print("Pacinte no encontrado")   
