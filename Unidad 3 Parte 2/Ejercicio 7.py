# Ejercicio 7
# Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún
# número negativo o no.

CANTIDAD_NUMEROS = 100
ha_habido_negativos = False

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

    if num < 0:
        ha_habido_negativos = True

if ha_habido_negativos:
    print("Se ha introducido al menos un número negativo.")
else:
    print("No se ha introducido ningún número negativo.")
