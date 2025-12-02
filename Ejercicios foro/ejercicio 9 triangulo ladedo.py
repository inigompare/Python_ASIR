# Triángulo ladeado (apuntando a la derecha)

# Solicitar al usuario la altura (anchura máxima)
n = int(input("Introduce la altura del triángulo: "))

# Parte superior (creciente)
for i in range(1, n + 1):
    if i == 1:
        print('*')
    else:
        # Borde izquierdo + espacios internos + borde derecho
        # Espacios internos siguen la serie impar: 1, 3, 5... (2*i - 3)
        print('*' + ' ' * (2 * i - 3) + '*')

# Parte inferior (decreciente)
for i in range(n - 1, 0, -1):
    if i == 1:
        print('*')
    else:
        # Borde izquierdo + espacios internos + borde derecho
        print('*' + ' ' * (2 * i - 3) + '*')
