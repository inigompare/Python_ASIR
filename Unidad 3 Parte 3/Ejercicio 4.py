# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
if num2 != 0:
    print(f"División: {num1 / num2}")
else:
    print("División: No se puede dividir por cero")
print(f"Multiplicación: {num1 * num2}")
