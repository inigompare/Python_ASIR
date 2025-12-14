# Ejercicio 8
# Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos
# son positivos y cuantos negativos.

CANTIDAD_NUMEROS = 100
positivos = 0
negativos = 0

print(f"Introduce {CANTIDAD_NUMEROS} números:")

for i in range(CANTIDAD_NUMEROS):
    while True:
        try:
            num = float(input(f"Número {i + 1}: "))
            if num != 0:
                break
            print("El número no debe ser nulo (0). Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    if num > 0:
        positivos += 1
    else:
        negativos += 1

print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")
