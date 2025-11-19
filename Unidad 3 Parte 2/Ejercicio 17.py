# Suma de números pares e impares entre 100 y 200
suma_pares = 0
suma_impares = 0
# Bucle para recorrer los números del 100 al 200
for numero in range(100, 201):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
# Resultados
print(f"Suma de pares: {suma_pares}")
print(f"Suma de impares: {suma_impares}")
