n = int(input("Introduce la altura de la pirámide: "))

for i in range(n):
    espacios = " " * (n - i - 1)

    # 1. La Cúspide (primera fila)
    if i == 0:
        print(espacios + "*")

    # 2. La Base (última fila) - Línea sólida
    elif i == n - 1:
        print(espacios + "*" * (2 * n - 1))

    # 3. La Mitad (fila central) - Línea punteada (* * * *)
    # Usamos n // 2 para encontrar el índice de la mitad entera
    elif i == n // 2:
        print(espacios + "* " * i + "*")

    # 4. Resto de filas - Huecas (* *)
    else:
        print(espacios + "*" + " " * (2 * i - 1) + "*")
