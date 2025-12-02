# Pedir la altura de la M
n = int(input("Introduce la altura de la M (número impar): "))

# Verificar si el número es par
if n % 2 == 0:
    print("Error: Introduce un número impar")
else:
    # Calcular el centro
    centro = n // 2

    # Recorrer cada fila
    for i in range(n):
        for j in range(n):
            # Condiciones para poner asterisco en la M:
            if j == 0 or j == n-1:
                # Lados verticales de la M
                print("*", end="")
            elif i <= centro and i == j:
                # Diagonal izquierda
                print("*", end="")
            elif i <= centro and i + j == n-1:
                # Diagonal derecha
                print("*", end="")
            else:
                print(" ", end="")
        print()
