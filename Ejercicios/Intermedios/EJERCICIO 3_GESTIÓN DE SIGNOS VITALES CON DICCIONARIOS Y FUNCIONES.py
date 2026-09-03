# ==========================================================
# EJERCICIO 3: GESTIÓN DE SIGNOS VITALES
# Nivel: Intermedio
# Tema: Salud (monitoreo)
#
# OBJETIVO:
# Usar diccionarios para almacenar múltiples registros,
# funciones para agregar y calcular promedios, y manejo de listas.
# ==========================================================

def registras_signos():
    print("\n--- Registrar signos vitales ---")
    nombre = input("Nombre del Paciente: ")
    temperatura = float(input("Temperatura (°C): "))
    frecuencia_cardiaca = int(input("Frecuencia cardiana (lpm): "))
    presion_sistolica = int(input("Presion sistolica: "))
    presion_diastolica = int(input("Presion diastolica: "))
    
    registro = {
        "nombre": nombre,
        "temperatura": temperatura,
        "frecuencia_cardiaca": frecuencia_cardiaca,
        "presion_sistolica": presion_sistolica,
        "presion_diastolica": presion_diastolica
    }
    
    return registro


def mostrar_registros(lista_registros):
    if not lista_registros:
        print("No hay registros")
        return
    print("\n--- REGSITROS DE SIGNOS VITALES ---")
    for i, registro in enumerate(lista_registros, start = 1):
        print(f"\nREgsitro {i}:")
        print(f"\Registro {i}: ")
        print(f" Paciente: {registro['nombre']}")
        print(f" Temperatura: {registro['temperatura']}°C")
        print(f" Frec. Cardiaca: {registro['frecuencia_cardiaca']} lpm")
        print(f" Presión {registro['presion_sistolica']}/{registro['presion_diastolica']} mmHg")
        
        
def calcular_promedio_temperatura(lista_registro):
    if not lista_registro:
        return None        
    total = sum(registro['temperatura'] for registro in lista_registro)
    return total / len(lista_registro)    


def main():
    registros = []
    while True:
        print("\n--- MENU SIGNOS VITALES ---")
        print("1. Agregar registro")
        print("2. Mostrar Todos los registros")
        print("3. Mostrar promedio de temperatura")
        print("4. Salir")
        opcion = input("opcion: ")
        if opcion == "1":
            nuevo = registras_signos()
            registros.append(nuevo)
            print("Registro agregado")
        elif opcion == "2":
            mostrar_registros(registros)
        elif opcion == "3":
            promedio = calcular_promedio_temperatura(registros)
            if promedio is None:
                print("No hay registros para calcular promedio")
            else:
                print(f"El promedio de temperatura es: {promedio:.2f}")
        elif opcion == "4":
            print("Saliendo . . . ")
            break
        else:
            print("OPCION NO VALIDA")
            
if __name__ == "__main__":
    main()