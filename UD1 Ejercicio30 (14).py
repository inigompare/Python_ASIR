# Pedimos el número N al usuario
n = int(input("Introduce un número entero (N): "))

print(f"Números del 1 al {n}:")
# Usamos 'n + 1' en el rango para que el bucle incluya a 'n'
for i in range(1, n + 1):
    print(i)
