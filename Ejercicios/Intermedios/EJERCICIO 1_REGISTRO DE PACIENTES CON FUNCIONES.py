# ==========================================================
# EJERCICIO 1: REGISTRO DE PACIENTES CON FUNCIONES
# Nivel: Intermedio
# Tema: Salud (administración)
#
# OBJETIVO:
# Aprender a definir funciones para modularizar el código,
# usar listas para almacenar datos y estructurar la interacción
# con el usuario a través de un menú.
# ==========================================================

def agregar_paciente(lista_pacientes):
    nombre = input("Nombre del paciente: ")
    edad = int(input("Edad: "))
    diagnostico = input("Diagnostico: ")
    
    paciente = {
        "nombre": nombre,
        "edad": edad,
        "diagnostico": diagnostico
    }
    
    lista_pacientes.append(paciente)
    
    print(f"Paciente {nombre} agregado correctamente")
    
def mostar_pacientes(lista_paciente):
    if not lista_paciente:
        print("No hat pacientes registrados")
        return
    
    print("\n--- LISTA DE PACIENTES ---")
    for paciente in lista_paciente:
        print(f"Nombre: {paciente['nombre']}, Edad: {paciente['edad']}, Diagnostico: {paciente['diagnostico']}")
        
def main():
    pacientes = []
    
    while True:
        print("\n--- SISTEMA DE REGISTRO DE PACIENTES ---")
        print("1. Agregar pacientes")
        print("2. Mostrar pacientes")
        print("3. Salir")
        opcion = input("Elige una opcion 1-3: ")
        
        if opcion == "1":
            agregar_paciente(pacientes)
        elif opcion == "2":
            mostar_pacientes(pacientes)
        elif opcion == "3":
            print("Saliendo del sistema . . .")
            break
        else:
            print("Opción no válidad, intenta de nuevo.")
            
if __name__ == "__main__":
    main()