# Introducir datos
altura = int(input("Introduce la altura de la pirámide invertida: "))
# Construir pirámide invertida
for i in range(altura, 0, -1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
