# Triángulo ladeado (apuntando a la izquierda)

# Solicitar al usuario la altura
n = int(input("Introduce la altura del triángulo: "))

# Parte superior (creciente hacia la izquierda)
for i in range(1, n + 1):
    if i == 1:
        # Primera fila: espacios para alinear a la derecha + asterisco
        print(' ' * (2 * n - 2) + '*')
    else:
        # Espacios iniciales + borde izquierdo + espacios internos + borde derecho
        espacios_iniciales = 2 * (n - i)
        espacios_internos = 2 * i - 3
        print(' ' * espacios_iniciales + '*' + ' ' * espacios_internos + '*')

# Parte inferior (decreciente)
for i in range(n - 1, 0, -1):
    if i == 1:
        # Última fila: espacios para alinear a la derecha + asterisco
        print(' ' * (2 * n - 2) + '*')
    else:
        # Espacios iniciales + borde izquierdo + espacios internos + borde derecho
        espacios_iniciales = 2 * (n - i)
        espacios_internos = 2 * i - 3
        print(' ' * espacios_iniciales + '*' + ' ' * espacios_internos + '*')
