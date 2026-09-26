# ==========================================================
# EJERCICIO 10: CONJUNTO DE MEDICAMENTOS PARA EVITAR DUPLICADOS
# Nivel: Intermedio
# Tema: Salud (medicación)
#
# OBJETIVO:
# Usar un conjunto (set) para almacenar medicamentos sin repeticiones.
# ==========================================================



medicamentos = set()

def agregar_medicamento(nombre):
    if nombre in medicamentos:
        print(f"{ nombre } ya esta en la lista. ")
    else:
        medicamentos.add(nombre)
        print(f"{ nombre } agregado .")

def listar_medicamento():
    if medicamentos:
        print("Medicamentos recetados: ")
        for med in medicamentos:
            print(f"- { med }")
    else:
        print("NO HAY MEDICAMENTOS .")

agregar_medicamento("Paracetamol")
agregar_medicamento("Ibupforeno")
agregar_medicamento("Paracetamol")
listar_medicamento()