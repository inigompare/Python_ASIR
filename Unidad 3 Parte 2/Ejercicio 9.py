# Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
# muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.

positivos = 0
negativos = 0
ha_habido_negativos = False

print("Introduce números (0 para terminar):")

while True:
    try:
        num = float(input("Introduce un número: "))
        if num == 0:
            break

        if num > 0:
            positivos += 1
        else:
            negativos += 1
            ha_habido_negativos = True

    except ValueError:
        print("Por favor, introduce un número válido.")

print("--- Resultados ---")
if ha_habido_negativos:
    print("Sí, se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")

print(f"Total de positivos: {positivos}")
print(f"Total de negativos: {negativos}")
