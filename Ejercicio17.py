# Entrada de datos
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Comprobamos si el primero ya es el más pequeño
if num1 < num2:
    print(f"Orden: {num1}, {num2}")
else:
    # Si no, el segundo debe ir primero (o son iguales)
    print(f"Orden: {num2}, {num1}")
