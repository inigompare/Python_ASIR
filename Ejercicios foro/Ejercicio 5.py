# Pedir el tamaño de la matriz
n = int(input("Introduce el tamaño de la matriz (n): "))

# Calcular el centro de la matriz
centro = n // 2

# Recorrer cada fila de la matriz
for i in range(n):
    # Recorrer cada columna de la fila
    for j in range(n):
        # Condiciones para poner asterisco:
        if i == centro or i == j or i + j == n-1:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
