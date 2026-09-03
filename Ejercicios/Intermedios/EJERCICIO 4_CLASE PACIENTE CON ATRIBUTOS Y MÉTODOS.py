# ==========================================================
# EJERCICIO 4: CLASE PACIENTE (POO BÁSICA)
# Nivel: Intermedio
# Tema: Salud (modelado de datos)
#
# OBJETIVO:
# Introducir la Programación Orientada a Objetos: definir una clase,
# crear objetos, usar el constructor __init__, métodos y atributos.
# ==========================================================

class Paciente:
    
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
        
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
    
    def mostrar_info(self):
        imc = self.calcular_imc()
        print(f"Paciente: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")
        print(f"IMC: {imc:.2f}")
    
if __name__ == "__main__":
    p1 = Paciente("Israel", 30, 65, 1.65)
    p1.mostrar_info()
    p2 = Paciente("Dante", 50, 80, 2.3)

