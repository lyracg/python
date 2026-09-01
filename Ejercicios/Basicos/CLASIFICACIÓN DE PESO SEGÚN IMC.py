peso = float(input("Peso (kg): "))
altura = float(input("Altua (m): "))
imc = peso / (altura ** 2)

print(f"Tu IMC es {imc:.1f}")

if imc < 18.5:
    print("Clasificación: Bajo Peso")
elif imc < 25:
    print("Clasificación: Peso Normal (Saludable")
elif imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificaicón: Obesidad")