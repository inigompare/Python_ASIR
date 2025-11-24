# Estrella de ocho puntas
n = int(input("Introduce un valor impar para n: "))

# Validación
if n % 2 == 0:
    print("n debe ser impar")
    exit()

# Centro de la figura
centro = (n + 1) // 2

# Recorremos filas
for i in range(1, n + 1):
    # Recorremos columnas
    for j in range(1, n + 1):

        # CONDICIONES:
        # Líneas que forman la estrella:
        # 1. Línea vertical central: j == centro
        # 2. Línea horizontal central: i == centro
        # 3. Diagonal principal: i == j
        # 4. Diagonal secundaria: i + j == n + 1

        if (
            j == centro or
            i == centro or
            i == j or
            i + j == n + 1
        ):
            print("*", end="")
        else:
            print(" ", end="")

    print()
