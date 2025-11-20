# Introducir datos
altura = int(input("Introduce la altura de la pirámide invertida: "))
# Construir pirámide invertida
for i in range(altura, 0, -1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
# Versión sencilla: calcula A^B sin usar **
altura = int(input("Introduce la altura de la pirámide: "))
# Construir pirámide
for i in range(1, altura + 1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
