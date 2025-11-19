# Contador
contador_positivos = 0
contador_negativos = 0

print("Introduce números (0 para terminar):")

# Este bucle se ejecutará para siempre hasta que encuentre un 'break'
while True:
    num = float(input("Número: "))

    # Condición de salida
    if num == 0:
        break  # Rompe el bucle

    # Si no es 0, lo contamos
    if num > 0:
        contador_positivos += 1  # 'a += 1' es lo mismo que 'a = a + 1'
    elif num < 0:
        contador_negativos += 1

print("\n--- Resultados ---")
print(f"Total de positivos: {contador_positivos}")
print(f"Total de negativos: {contador_negativos}")

if contador_negativos > 0:
    print("Sí, se ha leído al menos un número negativo.")
else:
    print("No se han leído números negativos.")
