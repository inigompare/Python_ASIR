import math

cantidad = int(input("¿Cuántos números primos quieres mostrar? "))

contador_primos = 0
numero = 2  # El primer número primo es el 2

while contador_primos < cantidad:
    es_primo = True
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print(numero)
        contador_primos += 1

    numero += 1
