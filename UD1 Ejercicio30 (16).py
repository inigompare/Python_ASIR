# Entrada de datos
print("Introduce dos números para compararlos:")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if num1 > num2:
    print(f"El mayor es: {num1}")
elif num2 > num1:
    print(f"El mayor es: {num2}")
else:
    print("Los dos números son iguales.")
