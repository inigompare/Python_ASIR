# Solicitar al usuario el tamaño del cuadrado
n = int(input("Introduce el tamaño del cuadrado: "))

# Calcular las dimensiones del cuadro interno
margen = n // 3
inicio_cuadro = margen
fin_cuadro = n - margen - 1

# Recorrer cada fila del cuadrado
for i in range(n):
    fila = ""

    for j in range(n):
        # Verificar si estamos en el área del cuadro interno (incluyendo bordes)
        if inicio_cuadro <= i <= fin_cuadro and inicio_cuadro <= j <= fin_cuadro:
            # Dentro del área del cuadro interno, solo dibujar los bordes
            if i == inicio_cuadro or i == fin_cuadro or j == inicio_cuadro or j == fin_cuadro:
                fila += '*'
            else:
                # Interior del cuadro: completamente vacío (sin diagonales)
                fila += ' '

        # Borde superior o inferior del cuadrado principal
        elif i == 0 or i == n - 1:
            fila += '*'

        # Borde izquierdo o derecho del cuadrado principal
        elif j == 0 or j == n - 1:
            fila += '*'

        # Diagonal principal (de arriba-izquierda a abajo-derecha)
        elif i == j:
            fila += '*'

        # Diagonal secundaria (de arriba-derecha a abajo-izquierda)
        elif i + j == n - 1:
            fila += '*'

        # Espacio vacío
        else:
            fila += ' '

    print(fila)
