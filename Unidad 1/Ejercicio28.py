# Suma de datos
suma_pares = 0
suma_impares = 0

# El rango 100-201 incluye el 100 y el 200
for num in range(100, 201):
    if num % 2 == 0:
        # El resto de dividir por 2 es 0 (es par)
        suma_pares += num
    else:
        # El resto es 1 (es impar)
        suma_impares += num

print(f"Suma de pares (100-200): {suma_pares}")
print(f"Suma de impares (100-200): {suma_impares}")
