import math

numero = int(input("Introduce un número entero: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
