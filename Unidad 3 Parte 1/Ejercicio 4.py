# Introducir datos
print("Introduce dos números para calcular:")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

# Calculamos las operaciones
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

# Muestra los resultados
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Producto: {num1} * {num2} = {producto}")

# Comprobamos la división por cero
if num2 != 0:
    division = num1 / num2
    print(f"División: {num1} / {num2} = {division}")
else:
    print("No se puede dividir por cero.")
