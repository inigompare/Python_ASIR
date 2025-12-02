# Triángulo ladeado (rombo) con solo bordes laterales - PRUEBA

# Valor de prueba
n = 7

# Primera mitad: creciente
for i in range(1, n + 1):
    if i == 1:
        # Primera fila: un solo asterisco centrado
        print(' ' * (n - 1) + '*')
    else:
        # Filas con dos asteriscos (bordes laterales)
        espacios_izquierda = n - i
        espacios_medio = 2 * i - 3
        print(' ' * espacios_izquierda + '*' + ' ' * espacios_medio + '*')

# Segunda mitad: decreciente
for i in range(n - 1, 0, -1):
    if i == 1:
        # Última fila: un solo asterisco centrado
        print(' ' * (n - 1) + '*')
    else:
        # Filas con dos asteriscos (bordes laterales)
        espacios_izquierda = n - i
        espacios_medio = 2 * i - 3
        print(' ' * espacios_izquierda + '*' + ' ' * espacios_medio + '*')
