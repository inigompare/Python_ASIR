# Dos contadores, empiezan en 0
contador_positivos = 0
contador_negativos = 0

print("Introduce 100 números (no nulos):")
# Bucle de 100 vueltas
for i in range(100):
    num = float(input(f"Número {i + 1}/100: "))

    if num > 0:
        # Si es positivo, sumamos 1 al contador de positivos
        contador_positivos = contador_positivos + 1
    elif num < 0:
        # Si es negativo, sumamos 1 al contador de negativos
        contador_negativos = contador_negativos + 1
    # Si es 0, no hace nada (el enunciado pide no nulos)

# Al final del bucle, mostramos los totales
print("\n--- Conteo Final ---")
print(f"Total de números positivos: {contador_positivos}")
print(f"Total de números negativos: {contador_negativos}")
