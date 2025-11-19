# Introducir datos
n = int(input("Introduce un número entero positivo (N): "))

# El factorial de 0 y 1 es 1
factorial = 1

if n < 0:
    print("No se puede calcular el factorial de un número negativo.")
elif n == 0:
    print("El factorial de 0 es: 1")
else:
    # Acumulamos la multiplicación en la variable 'factorial'
    # El bucle va desde 1 hasta n (incluida)
    for i in range(1, n + 1):
        factorial = factorial * i
        # 1ª vuelta: factorial = 1 * 1 (vale 1)
        # 2ª vuelta: factorial = 1 * 2 (vale 2)
        # 3ª vuelta: factorial = 2 * 3 (vale 6)
        # ...

    print(f"El factorial de {n} es: {factorial}")
