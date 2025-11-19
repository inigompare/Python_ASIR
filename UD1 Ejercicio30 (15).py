# Entrada de datos
print("Introduce dos números para calcular:")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

# Calculamos e imprimimos directamente
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Producto: {num1 * num2}")

# Comprobamos la división por cero (el rombo)
if num2 != 0:
    print(f"División: {num1 / num2}")
else:
    print("Error: No se puede dividir por cero.")
