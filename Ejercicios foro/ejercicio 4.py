# Programa que dibuja un cuadrado con bordes y diagonales marcadas con asteriscos

# Pedir la altura del cuadrado
n = int(input("Introduce el lado del cuadrado (n): "))

# Recorrer cada fila del cuadrado
for i in range(n):
    # Recorrer cada columna de la fila
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n-1:
            print("*", end="")
        else:
            print(" ", end="")

    # Salto de línea al terminar cada fila
    print()
