# Diamante hueco
n = int(input("Introduce el valor de n para el diamante: "))

# El tamaño total de la cuadrícula es 2*n - 1
tamano = 2 * n - 1

# Bucle
for i in range(1, tamano + 1):
    # Bucle para las columnas
    for j in range(1, tamano + 1):

        # CONDICIÓN:
        # Calculamos la distancia al centro (n, n)
        # Si la suma de distancias vertical y horizontal es n-1, pintamos asterisco
        if abs(i - n) + abs(j - n) == n - 1:
            print("*", end="")  # Asterisco
        else:
            print(" ", end="")  # Espacio hueco

    print()  # Salto de línea al final de cada fila
