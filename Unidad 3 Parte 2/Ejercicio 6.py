# Ejercicio 6
# Programa que lea un número positivo N y calcule y visualice su factorial N!

while True:
    try:
        n = int(input("Introduce un número positivo: "))
        if n >= 0:
            break
        print("El número debe ser positivo.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

factorial = 1
# Calculamos el factorial
# Si n es 0, el rango (1, 1) es vacío y el factorial queda en 1, lo cual es correcto (0! = 1)
for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} ({n}!) es: {factorial}")
